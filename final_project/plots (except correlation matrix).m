clear
clc

%% Pre-proccesings

% Band-pass filter
cfg = [];
cfg.bpfilter = 'yes';
cfg.bpfreq = [0.05 60];
cfg.bpfiltord = 4;
cfg.bpfilttype = 'but';
cfg.bfiltdir = 'twopass';

% Baseline-correction 
cfg.demean          = 'yes';
cfg.baselinewindow  = [-0.3 0];

% Downsampling
cfg.resamplefs = 600;

EEG = [];
files = dir('*.mat');
N = length(files);  % total number of files 
% loop for each file 
for i = 1:N
    cfg.inputfile = files(i).name;
    EEG{i,1} = cfg.inputfile;
    EEG{i,2} = ft_resampledata(cfg);
    ch1_mean = cat(3,EEG{i,2}.trial{:});
    EEG{i,3} = mean(ch1_mean(1,:,:), 3);
end

%% Amplitude Ploting

h1 = figure();
subplot(2,2,1)
hold on
for i = 1:10
    plot(EEG{i,2}.time{1}, EEG{i,3}, 'Linewidth', 1, 'DisplayName', erase(EEG{i,1},'.mat'));
    title('Control Group AEPs'); 
    xlabel('Time(s)'); ylabel('Amplitude(\muV)');
    ylim([-100 200]); xlim([-0.2 0.6]);
end
legend
hold off
subplot(2,2,2)
hold on
for i = 11:17
    plot(EEG{i,2}.time{1}, EEG{i,3}, 'Linewidth', 1, 'DisplayName', erase(EEG{i,1},'.mat'));
    title('Mild Group AEPs'); 
    xlabel('Time(s)'); ylabel('Amplitude(\muV)');
    ylim([-100 200]); xlim([-0.2 0.6]);
end
legend
hold off
subplot(2,2,3)
hold on
for i = 18:24
    plot(EEG{i,2}.time{1}, EEG{i,3}, 'Linewidth', 1, 'DisplayName', erase(EEG{i,1},'.mat'));
    title('Moderate Group AEPs'); 
    xlabel('Time(s)'); ylabel('Amplitude(\muV)');
    ylim([-100 200]); xlim([-0.2 0.6]);
end
legend
hold off
subplot(2,2,4)
hold on
for i = 25:31
    plot(EEG{i,2}.time{1}, EEG{i,3}, 'Linewidth', 1, 'DisplayName', erase(EEG{i,1},'.mat'));
    title('Severe Group AEPs'); 
    xlabel('Time(s)'); ylabel('Amplitude(\muV)');
    ylim([-100 200]); xlim([-0.2 0.6]);
end
legend
hold off

%-----------------------------------------------

% calculating confidence intervals with respect to central limit theorem
control_ave = squeeze(cat(3,EEG{1:10,3}));
mild_ave = squeeze(cat(3,EEG{11:17,3}));
moderate_ave = squeeze(cat(3,EEG{18:24,3}));
severe_ave = squeeze(cat(3,EEG{25:31,3}));

control = [mean(control_ave')+2/sqrt(10)*std(control_ave') fliplr(mean(control_ave')-2/sqrt(10)*std(control_ave'))];
mild = [mean(mild_ave')+2/sqrt(7)*std(mild_ave') fliplr(mean(mild_ave')-2/sqrt(7)*std(mild_ave'))];
moderate = [mean(moderate_ave')+2/sqrt(7)*std(moderate_ave') fliplr(mean(moderate_ave')-2/sqrt(7)*std(moderate_ave'))];
severe = [mean(severe_ave')+2/sqrt(7)*std(severe_ave') fliplr(mean(severe_ave')-2/sqrt(7)*std(severe_ave'))];

% ploting
x = EEG{25,2}.time{1};
xconf = [x fliplr(x)];
h2 = figure();
subplot(2,2,1)
hold on
fill(xconf, control, [0 0.4470 0.7410], 'EdgeColor', 'none', 'FaceAlpha', 0.2)
plot(x, mean(control_ave'), 'color', [0 0.4470 0.7410], 'Linewidth', 1)
title('Control Group AEPs'); 
xlabel('Time(s)'); ylabel('Amplitude(\muV)');
ylim([-100 200]); xlim([-0.2 0.6]);
hold off
subplot(2,2,2)
hold on
fill(xconf, mild, [0.8500 0.3250 0.0980], 'EdgeColor', 'none', 'FaceAlpha', 0.2)
plot(x, mean(mild_ave'), 'color', [0.8500 0.3250 0.0980], 'Linewidth', 1)
title('Mild Stroke Group AEPs'); 
xlabel('Time(s)'); ylabel('Amplitude(\muV)');
ylim([-100 200]); xlim([-0.2 0.6]);
hold off
subplot(2,2,3)
hold on
fill(xconf, moderate, [0.9290 0.6940 0.1250], 'EdgeColor', 'none', 'FaceAlpha', 0.2)
plot(x, mean(moderate_ave'), 'color', [0.9290 0.6940 0.1250], 'Linewidth', 1)
title('Moderate Stroke Group AEPs'); 
xlabel('Time(s)'); ylabel('Amplitude(\muV)');
ylim([-100 200]); xlim([-0.2 0.6]);
hold off
subplot(2,2,4)
hold on
fill(xconf, severe, [0.4940 0.1840 0.5560], 'EdgeColor', 'none', 'FaceAlpha', 0.2)
plot(x, mean(severe_ave'), 'color', [0.4940 0.1840 0.5560], 'Linewidth', 1)
title('Severe Stroke Group AEPs'); 
xlabel('Time(s)'); ylabel('Amplitude(\muV)');
ylim([-100 200]); xlim([-0.2 0.6]);
hold off

%-----------------------------------------------

h3 = figure();
hold on
plot(EEG{1,2}.time{1}, mean(control_ave'), 'Linewidth', 2, 'DisplayName', 'Control');
plot(EEG{11,2}.time{1}, mean(mild_ave'), 'Linewidth', 2, 'DisplayName', 'Mild Stroke');
plot(EEG{18,2}.time{1}, mean(moderate_ave'), 'Linewidth', 2, 'DisplayName', 'Moderate Stroke');
plot(EEG{25,2}.time{1}, mean(severe_ave'), 'Linewidth', 2, 'DisplayName', 'Severe Stroke');
hold off
title('Average AEPs'); 
xlabel('Time(s)'); ylabel('Amplitude(\muV)');
ylim([-100 200]); xlim([-0.2 0.6]);
legend
