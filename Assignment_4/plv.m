function PLV = plv(eeg, samplerate, freqrange, order)
% number of trials
n = size(eeg, 3);

% filtering
a = fir1(order, 2/samplerate*freqrange);
filteredeeg = filter(a, 1, eeg, [], 2);

% hilbert transform
phi1 = angle(hilbert(squeeze(filteredeeg(1, :, :))));
phi2 = angle(hilbert(squeeze(filteredeeg(2, :, :))));

% average exponentiated phase difference over trials
PLV = (1/n)*abs(sum(exp(1i*(phi1 - phi2)), 2));

return;