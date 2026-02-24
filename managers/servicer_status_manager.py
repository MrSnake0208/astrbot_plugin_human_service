"""
客服状态管理器
负责管理客服的在线/离线状态
"""


class ServicerStatusManager:
    """客服状态管理器 - 管理客服在线/离线状态"""

    def __init__(self, servicer_ids: list):
        """
        初始化客服状态管理器

        Args:
            servicer_ids: 客服ID列表
        """
        # 默认所有客服为在线状态
        self.status_map = {sid: "online" for sid in servicer_ids}
        # 离线期间的通知累积 {servicer_id: [通知列表]}
        self.pending_notifications = {sid: [] for sid in servicer_ids}

    def set_online(self, servicer_id: str) -> bool:
        """
        设置客服为在线状态

        Args:
            servicer_id: 客服ID

        Returns:
            bool: 是否设置成功
        """
        if servicer_id in self.status_map:
            self.status_map[servicer_id] = "online"
            return True
        return False

    def set_offline(self, servicer_id: str) -> bool:
        """
        设置客服为离线状态

        Args:
            servicer_id: 客服ID

        Returns:
            bool: 是否设置成功
        """
        if servicer_id in self.status_map:
            self.status_map[servicer_id] = "offline"
            return True
        return False

    def is_online(self, servicer_id: str) -> bool:
        """
        检查客服是否在线

        Args:
            servicer_id: 客服ID

        Returns:
            bool: 是否在线（默认在线）
        """
        return self.status_map.get(servicer_id, "online") == "online"

    def get_status(self, servicer_id: str) -> str:
        """
        获取客服状态

        Args:
            servicer_id: 客服ID

        Returns:
            str: "online" 或 "offline"
        """
        return self.status_map.get(servicer_id, "online")

    def add_servicer(self, servicer_id: str):
        """
        添加新客服（默认为在线状态）

        Args:
            servicer_id: 客服ID
        """
        if servicer_id not in self.status_map:
            self.status_map[servicer_id] = "online"
            self.pending_notifications[servicer_id] = []

    def add_pending_notification(self, servicer_id: str, notification: dict):
        """
        添加离线通知

        Args:
            servicer_id: 客服ID
            notification: 通知内容字典，包含 user_id, name, group_id, timestamp, type 等信息
        """
        if servicer_id in self.pending_notifications:
            self.pending_notifications[servicer_id].append(notification)

    def get_and_clear_pending(self, servicer_id: str) -> list:
        """
        获取并清空离线通知列表

        Args:
            servicer_id: 客服ID

        Returns:
            list: 离线期间累积的通知列表
        """
        notifications = self.pending_notifications.get(servicer_id, [])
        self.pending_notifications[servicer_id] = []
        return notifications

    def is_in_offline_mode(self, servicer_id: str) -> bool:
        """
        检查客服是否处于离线模式（即是否离线）

        Args:
            servicer_id: 客服ID

        Returns:
            bool: 是否处于离线模式
        """
        return self.status_map.get(servicer_id, "online") == "offline"

    def has_any_online_servicer(self) -> bool:
        """
        检查是否有任何在线的客服

        Returns:
            bool: 是否有任何客服在线
        """
        return any(status == "online" for status in self.status_map.values())
