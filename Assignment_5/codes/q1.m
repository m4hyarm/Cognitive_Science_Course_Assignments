clc
clear

%% 1.1 %%

% a
load extracellular.mat
x = all_data_with_noise_and_line;
fs= 2400;   % sample frequency
t = 1/fs;   % sample time
T = t:t:length(x)/fs;

figure
plot(T, x)
xlabel('Time (s)')
ylabel('Voltage Amplitude (\muv)')
title('Amplitude Against Time')

% b
figure
histogram(x)
xlabel('Voltage Amplitude (\muv)')
ylabel('Count')
title('Histogram of recorded Amplitude')


%% 1.2 %%

% c
fc = 300;   % cut off frequency
order = 7;  % 6th order
[b, a] = butter(order,fc/(fs/2),'high');
y = filtfilt(b,a,x);

% d
figure
hold on
plot(T,x)
plot(T,y)
legend('Noisy Signal','High-pass Filtered')
xlabel('Time (s)')
ylabel('Voltage Amplitude (\muv)')
xlim([1 2])
title('Amplitude Against Time for 2 Seconds')
hold off

%% 1.3 %%

% e
sigma = median(abs(y)/0.6745);
theta = 5*sigma;

% f
Y_abs = abs(y);
[pks, pklocs] = findpeaks(Y_abs);                           
peaks = cat(2, pklocs', y(pklocs)'); 

% g
spikes = peaks(abs(peaks(:,2)) >= theta, :);
time = round(2*2400/1000);
waveforms = zeros(length(spikes), 2*time+1);

% h
figure
T = -2:4/10:2;
hold on
for i = 1:length(spikes)
    idx = spikes(i,1);
    waveform = y(idx-time:idx+time);
    plot(T, waveform);
    waveforms(i,:) = waveform;
end
title('Detected waveforms')
xlabel('Time (ms)')
ylabel('Voltage Amplitude (\muv)')
hold off

%% 1.4 %%

% i
[coeff,score,latent] = pca(waveforms);

% j
PCs = score(:,1:3);

%% 1.5 %%

figure
Ks = 6;
n = 1;
for i = 2:Ks
    [idx,C,sumd,D] = kmeans(PCs, i);
    for j = 1:i
        subplot(Ks,3,n)
        hold on
        plot(PCs(idx == j,1),PCs(idx == j,2), '.')
        xlabel('PC1'), ylabel('PC2'), title(sprintf('K = %d',i))
        xticks([]), yticks([])
        hold off
        subplot(Ks,3,n+1)
        hold on
        plot(PCs(idx == j,1),PCs(idx == j,3), '.')
        xlabel('PC1'), ylabel('PC3'), title(sprintf('K = %d',i))
        xticks([]), yticks([])
        hold off
        subplot(Ks,3,n+2)
        hold on
        plot(PCs(idx == j,2),PCs(idx == j,3), '.')
        xlabel('PC2'), ylabel('PC3'), title(sprintf('K = %d',i))
        xticks([]), yticks([])
        hold off
    end
    n = n + 3;
end
sgtitle('Kmeans Clustring with PCA Feature Extraction')


%% questions: n

load spikes.mat
grand_truth = SpikeInds;
detected_spikes = spikes(:,1)';
all_times = 1:length(y);
TP = length(intersect(grand_truth, detected_spikes));
TN = length(intersect(setdiff(all_times, grand_truth), setdiff(all_times, detected_spikes)));
FP = length(intersect(detected_spikes, setdiff(all_times, grand_truth)));
FN = length(intersect(grand_truth, setdiff(all_times, detected_spikes)));

recall = TP/(TP+FN);
precision = TP/(TP+FP);
CM = [TP FP; FN TN];

figure
h = heatmap(CM, 'XData', ["True" "False"], 'YData', ["True" "False"]);
h.FontSize = 15;
xlabel('Actual')
ylabel('Detected')
title(sprintf('Confusion Matrix \n(Recall: %.2f / Precision: %.2f)',recall,precision));


%% questions: o

new_theta = 0.9*max(Y_abs);
spikes_2 = peaks(abs(peaks(:,2)) >= new_theta, :);
waveframes_2 = zeros(length(spikes_2), 2*time+1);

figure
T = -2:4/10:2;
hold on
for i = 1:length(spikes_2)
    idx = spikes_2(i,1);
    waveform = y(idx-time:idx+time);
    plot(T, waveform);
    waveframes_2(i,:) = waveform;
end
title('Detected waveforms')
xlabel('Time (ms)')
ylabel('Voltage Amplitude (\muv)')
hold off


%% questions: p

Y = tsne(waveforms,'NumDimensions',3);
figure
Ks = 6;
n = 1;
for i = 2:Ks
    [idx,C,sumd,D] = kmeans(PCs, i);
    for j = 1:i
        subplot(Ks,3,n)
        hold on
        plot(Y(idx == j,1),Y(idx == j,2), '.')
        xlabel('F1'), ylabel('F2'), title(sprintf('K = %d',i))
        xticks([]), yticks([])
        hold off
        subplot(Ks,3,n+1)
        hold on
        plot(Y(idx == j,1),Y(idx == j,3), '.')
        xlabel('F1'), ylabel('F3'), title(sprintf('K = %d',i))
        xticks([]), yticks([])
        hold off
        subplot(Ks,3,n+2)
        hold on
        plot(Y(idx == j,2),Y(idx == j,3), '.')
        xlabel('F2'), ylabel('F3'), title(sprintf('K = %d',i))
        xticks([]), yticks([])
        hold off
    end
    n = n + 3;
end
sgtitle('Kmeans Clustring with t-SNE Feature Extraction')

