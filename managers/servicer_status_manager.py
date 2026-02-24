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
