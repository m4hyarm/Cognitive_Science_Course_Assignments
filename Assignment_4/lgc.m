function [two_one,one_two] = lgc(lfp, timestep, timewind, order)

nobs = size(lfp, 2);             % number of observations
ek    = timewind:timestep:nobs;  % GC evaluation points
enobs = length(ek);              % number of GC evaluations

two_one = zeros(enobs,1);
one_two = zeros(enobs,1);
for e = 1:enobs
    j = ek(e);
    [FF,~,~,~] = GCCA_tsdata_to_pwcgc(lfp(:,j-timewind+1:j,:),order,'OLS');
    two_one(e) = FF(1,2);  % estimated GC 2 -> 1
    one_two(e) = FF(2,1);  % estimated GC 1 -> 2
end

return;