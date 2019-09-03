local oldState = 'NONE'
local newState = 'NONE'
local action = 'IGNORE'
if (redis.call('EXISTS', KEYS[1]) == 1) then
    oldState = redis.call('GET', KEYS[1])
    if (ARGV[1] == 'MGMT_GET_SESS') then
        action = "PSE_CONT_OLD_EXIST"
        return { oldState, newState, action }
    elseif (ARGV[1] == 'MGMT_REL_SESS') then
        action = "SMF_REL"
	    redis.call('SET', KEYS[1], 'REL_WT_N2_ACK')
        newState = redis.call('GET', KEYS[1])
        return { oldState, newState, action }
    end
    if (ARGV[1] == 'PSE_CC_REQ') then
        action = 'PSE_CONT_OLD_EXIST'
    elseif (oldState == 'PENDING') then
        if (ARGV[1] == 'PSE_N1N2_RSP') then
            redis.call('SET', KEYS[1], 'WT_SETUP')
            newState = redis.call('GET', KEYS[1])
            action = 'SETUP_CONT'
        elseif (ARGV[1] == 'UC_SETUP_RSP') then
            action = 'QUEUE'
        elseif (ARGV[1] == 'UC_SETUP_FAIL') then
            action = 'QUEUE'
        elseif (ARGV[1] == 'UPSR_UC_REL_REQ') then
            redis.call('SET', KEYS[1], 'WT_SETUP')
            newState = redis.call('GET', KEYS[1])
            action = 'UPSR_CONT'
        else
            action = 'IGNORE'
        end
    elseif (oldState == 'WT_SETUP') then
        if (ARGV[1] == 'UC_SETUP_RSP') then
            redis.call('SET', KEYS[1], 'ACTIVE')
            newState = redis.call('GET', KEYS[1])
            action = 'UC_CONT'
        elseif (ARGV[1] == 'UC_SETUP_FAIL') then
            redis.call('SET', KEYS[1], 'REL_WT_N1N2')
            newState = redis.call('GET', KEYS[1])
            action = 'NPSR_CONT'
        elseif (ARGV[1] == 'UPSR_UC_REL_REQ') then
            redis.call('SET', KEYS[1], 'REL_WT_N2_ACK')
            newState = redis.call('GET', KEYS[1])
            action = 'UPSR_CONT'
        else
            action = 'IGNORE'
        end
    elseif (oldState == 'ACTIVE') then
        if (ARGV[1] == 'UPSM_UC_MOD_REQ') then
            redis.call('SET', KEYS[1], 'MOD_WT_N2_ACK')
            newState = redis.call('GET', KEYS[1])
            action = 'UPSM_CONT'
        elseif (ARGV[1] == 'NPSM_MOD_CMD') then
            redis.call('SET', KEYS[1], 'MOD_WT_N2_ACK')
            newState = redis.call('GET', KEYS[1])
            action = 'PSM_CONT'
        elseif (ARGV[1] == 'UC_DEACTIVATE') then
            redis.call('SET', KEYS[1], 'IDLE')
            newState = redis.call('GET', KEYS[1])
            action = 'AN_REL'
        elseif (ARGV[1] == 'UPSR_UC_REL_REQ') then
            redis.call('SET', KEYS[1], 'REL_WT_N2_ACK')
            newState = redis.call('GET', KEYS[1])
            action = 'UPSR_CONT'
        else
            action = 'IGNORE'
        end
    elseif (oldState == 'MOD_WT_N2_ACK') then
        if (ARGV[1] == 'N2_MOD_ACK') then
            redis.call('SET', KEYS[1], 'MOD_WT_N1_ACK')
            newState = redis.call('GET', KEYS[1])
            action = 'PSM_CONT'
        elseif (ARGV[1] == 'N2_MOD_NACK') then
            redis.call('SET', KEYS[1], 'ACTIVE')
            newState = redis.call('GET', KEYS[1])
            action = 'PSM_FAIL'
        elseif (ARGV[1] == 'N1_MOD_ACK') then
            action = 'QUEUE'
        elseif (ARGV[1] == 'N1_MOD_NACK') then
            action = 'QUEUE'
        elseif (ARGV[1] == 'UPSR_UC_REL_REQ') then
            redis.call('SET', KEYS[1], 'REL_WT_N2_ACK')
            newState = redis.call('GET', KEYS[1])
            action = 'UPSR_CONT'
        else
            action = 'IGNORE'
        end
    elseif (oldState == 'MOD_WT_N1_ACK') then
        if (ARGV[1] == 'N1_MOD_ACK') then
            redis.call('SET', KEYS[1], 'ACTIVE')
            newState = redis.call('GET', KEYS[1])
            action = 'PSM_CONT'
        elseif (ARGV[1] == 'N1_MOD_NACK') then
            redis.call('SET', KEYS[1], 'ACTIVE')
            newState = redis.call('GET', KEYS[1])
            action = 'PSM_FAIL'
        elseif (ARGV[1] == 'UPSR_UC_REL_REQ') then
            redis.call('SET', KEYS[1], 'REL_WT_N2_ACK')
            newState = redis.call('GET', KEYS[1])
            action = 'UPSR_CONT'
        else
            action = 'IGNORE'
        end
    elseif (oldState == 'REL_WT_N2_ACK') then
        if (ARGV[1] == 'N2_REL_ACK') then
            redis.call('SET', KEYS[1], 'REL_WT_N1_ACK')
            newState = redis.call('GET', KEYS[1])
            action = 'PSM_CONT'
        elseif (ARGV[1] == 'N1_REL_ACK') then
            action = 'QUEUE'
        else
            action = 'IGNORE'
        end
    elseif (oldState == 'REL_WT_N1_ACK') then
        if (ARGV[1] == 'N1_REL_ACK') then
            redis.call('SET', KEYS[1], 'NONE')
            newState = redis.call('GET', KEYS[1])
            action = 'STATUS_NTY_REL'
        else
            action = 'IGNORE'
        end
    elseif (oldState == 'IDLE') then
        if (ARGV[1] == 'UC_ACTIVATE') then
            redis.call('SET', KEYS[1], 'WT_SETUP')
            newState = redis.call('GET', KEYS[1])
            action = 'USR_CONT'
        else
            action = 'IGNORE'
        end
    end
else
    if (ARGV[1] == 'PSE_CC_REQ') then
        redis.call('SET', KEYS[1], 'PENDING')
        newState = 'PENDING'
        action = 'PSE_CONT'
    elseif (ARGV[1] == 'MGMT_GET_SESS') then
        action = 'IGNORE_NO_EXIST'
    elseif (ARGV[1] == 'MGMT_REL_SESS') then
        action = 'IGNORE_NO_EXIST'
    elseif (ARGV[1] == 'PSR_RC_REQ') then
        action = 'IGNORE_NO_EXIST'
    else
        action = 'IGNORE'
    end
end
return {oldState, newState, action}
