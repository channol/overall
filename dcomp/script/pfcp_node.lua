--[[--
File              : pfcp_node.lua
Author            : zcy
Date              : 2019-06-14 17:28:56
Last Modified Date: 2019-06-14 17:28:56
--]]--
if (redis.call("EXISTS", KEYS[1]) == 1) then
    return 1
else
    redis.call("SET", KEYS[1], ARGV[1])
    return 0
end

    
