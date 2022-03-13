#!/usr/bin/env python3

# constants for pero worker

# zookeeper paths

PERO_PATH = '/pero'

WORKER_STATUS = PERO_PATH + '/worker/status'
WORKER_STATUS_ID_TEMPLATE = WORKER_STATUS + '/{worker_id}'
WORKER_STATUS_TEMPLATE = WORKER_STATUS_ID_TEMPLATE + '/status'  # current worker status
WORKER_QUEUE_TEMPLATE = WORKER_STATUS_ID_TEMPLATE + '/queue'  # input queue
WORKER_ENABLED_TEMPLATE = WORKER_STATUS_ID_TEMPLATE + '/enabled'  # worker enabled

WORKER_CONFIG = PERO_PATH + '/worker/config'  # configs for all workers
WORKER_CONFIG_MQ_SERVERS = WORKER_CONFIG + '/mq_servers'
WORKER_CONFIG_FTP_SERVERS = WORKER_CONFIG + '/ftp_servers'
WORKER_CONFIG_REDIS_SERVERS = WORKER_CONFIG + '/redis_servers'

QUEUE = PERO_PATH + '/queue'
QUEUE_TEMPLATE = QUEUE + '/{queue_name}'
QUEUE_CONFIG_TEMPLATE = QUEUE_TEMPLATE + '/config'  # configs for processing (config.ini)
QUEUE_STATS_AVG_MSG_TIME_TEMPLATE = QUEUE_TEMPLATE + '/avg_msg_time'  # average time needed for processing message from this queue
QUEUE_STATS_WAITING_SINCE_TEMPLATE = QUEUE_TEMPLATE + '/waiting_since'  # time when oldest message was written to the queue
QUEUE_STATS_ADMINISTRATIVE_PRIORITY_TEMPLATE = QUEUE_TEMPLATE + '/administrative_priority'  # priority set by administrator to prefer queue

# zookeeper int data settings
ZK_INT_BYTEORDER = 'big'  # Big endian - MSB is at the beginning of the byte object

# worker status
STATUS_STARTING = 'STARTING'
STATUS_PROCESSING = 'PROCESSING'
STATUS_RECONFIGURING = 'RECONFIGURING'
STATUS_IDLE = 'IDLE'
STATUS_FAILED = 'FAILED'
STATUS_DEAD = 'DEAD'

