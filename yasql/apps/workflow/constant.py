# -*- coding:utf-8 -*-
# by pandonglin

STATE_TYPE_START = 1  # 开始
STATE_TYPE_END = 2    # 结束

TICKET_ACT_STATE_DRAFT = 0    # 初始化
TICKET_ACT_STATE_DOING = 1  # 进行中
TICKET_ACT_STATE_PASS = 2     # 已通过
TICKET_ACT_STATE_REFUSE = 3   # 已拒绝
TICKET_ACT_STATE_FINISH = 4   # 已完成
TICKET_ACT_STATE_FAIL = 5     # 已失败
TICKET_ACT_STATE_CLOSE = 6   # 已关闭
TICKET_ACT_STATE_STOP = 7     # 已中止

TICKET_ACT_STATE_END = [TICKET_ACT_STATE_REFUSE, TICKET_ACT_STATE_FINISH, TICKET_ACT_STATE_CLOSE, TICKET_ACT_STATE_STOP]

TICKET_ACT_STATE_MAP = (
    (TICKET_ACT_STATE_DRAFT, "初始化"),
    (TICKET_ACT_STATE_DOING, "进行中"),
    (TICKET_ACT_STATE_PASS, "已通过"),
    (TICKET_ACT_STATE_REFUSE, "已拒绝"),
    (TICKET_ACT_STATE_FINISH, "已完成"),
    (TICKET_ACT_STATE_FAIL, "已失败"),
    (TICKET_ACT_STATE_CLOSE, "已关闭"),
    (TICKET_ACT_STATE_STOP, "已中止"),
)


PARTICIPANT_TYPE_PERSONAL = 1  # 个人
PARTICIPANT_TYPE_ROLE = 2      # 角色
PARTICIPANT_TYPE_ROBOT = 3     # 机器人，脚本
PARTICIPANT_TYPE_FIELD = 4     # 工单字段(用户名类型的)
PARTICIPANT_TYPE_HOOK = 5      # hook方式

PARTICIPANT_TYPE = (
    (PARTICIPANT_TYPE_PERSONAL, "个人"),
    (PARTICIPANT_TYPE_ROLE, "角色"),
    (PARTICIPANT_TYPE_ROBOT, "机器人"),
    (PARTICIPANT_TYPE_FIELD, "工单字段"),
    (PARTICIPANT_TYPE_HOOK, "Hook"),  # 第3方
)

TRANSITION_TYPE_COMMON = 1  # 常规流转
TRANSITION_TYPE_TIMER = 2   # 其他

TRANSITION_ATTRIBUTE_TYPE_ACCEPT = 1  # 同意
TRANSITION_ATTRIBUTE_TYPE_REFUSE = 2  # 拒绝
TRANSITION_ATTRIBUTE_TYPE_TIMEOUT = 3   # 超时
TRANSITION_ATTRIBUTE_TYPE_OTHER = 4   # 其他

FIELD_ATTRIBUTE_RO = 1  # 只读
FIELD_ATTRIBUTE_REQUIRED = 2  # 必填
FIELD_ATTRIBUTE_OPTIONAL = 3  # 可选