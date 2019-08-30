local subID = ''
local exist = 0
if (redis.call('EXISTS', KEYS[1]) == 1) then
    subID = redis.call('GET', KEYS[1])
    exist = 1
    if (string.len(ARGV[1]) ~= 0) then
        redis.call('SET', KEYS[1], ARGV[1])
    end
else
    redis.call('SET', KEYS[1], '')
    exist = 0
end
return {subID, exist}
