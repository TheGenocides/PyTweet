import datetime
from typing import Any, Dict, List, Optional

from .enums import SpaceState
from .utils import time_parse_todt
from .user import User
from .dataclass import SpaceTopic

__all__ = ("Space",)


class Space:
    """Represents a twitter space.

    .. versionadded:: 1.3.5
    """

    __slots__ = ("__original_payload", "_payload", "http_client", "_include")

    def __init__(self, data: Dict[str, Any], http_client: object):
        self.__original_payload = data
        self._payload = None
        self.http_client = http_client

        try:
            if isinstance(data.get("data"), list):
                self._payload = data.get("data")[0]
            else:
                self._payload = data.get("data")
        except AttributeError:
            self._payload = self.__original_payload
        self._include = self.__original_payload.get("includes")

    def __repr__(self) -> str:
        return "Space(name={0.title} id={0.id} state={0.state})".format(self)

    @property
    def title(self) -> str:
        """:class:`str`: The space's title.

        .. versionadded:: 1.3.5
        """
        return self._payload.get("title")

    @property
    def raw_state(self) -> str:
        """:class:`str`: The raw space's state in  a string.

        .. versionadded:: 1.3.5
        """
        return self._payload.get("state")

    @property
    def state(self) -> SpaceState:
        """:class:`SpaceState`: The type of the space's state.

        .. versionadded:: 1.3.5
        """
        return SpaceState(self.raw_state)

    @property
    def id(self) -> str:
        """:class:`str`: The space's unique id.

        .. versionadded:: 1.3.5
        """
        return self._payload.get("id")

    @property
    def lang(self) -> str:
        """:class:`str`: The space's language.

        .. versionadded:: 1.3.5
        """
        return self._payload.get("lang")

    @property
    def created_at(self) -> datetime.datetime:
        """:class:`datetime.datetime`: Returns a datetime.datetime object with the space's created datetime.

        .. versionadded:: 1.3.5
        """
        return time_parse_todt(self._payload.get("created_at"))

    @property
    def started_at(self) -> Optional[datetime.datetime]:
        """Optional[:class:`datetime.datetime`]: Returns a datetime.datetime object with the space's started time. Only available if the space has started.

        .. versionadded:: 1.3.5
        """
        return time_parse_todt(self._payload.get("started_at")) if self._payload.get("started_at") else None

    @property
    def updated_at(self) -> Optional[datetime.datetime]:
        """Optional[:class:`datetime.datetime`]: Returns a datetime.datetime object with the space's last update to any of this Space's metadata, such as the title or scheduled time. Only available if the space has started.

        .. versionadded:: 1.3.5
        """
        return time_parse_todt(self._payload.get("updated_at"))

    @property
    def ticketed(self) -> bool:
        """Returns a bool indicate if the space is ticketed.

        Returns
        ---------
        :class:`bool`
            This method returns a :class:`bool` object.


        .. versionadded:: 1.5.0
        """
        return self._payload.get("is_ticketed")

    def fetch_creator(self) -> User:
        """Fetches the creator's using the id.

        Returns
        ---------
        :class:`User`
            This method returns a :class`User` object.


        .. versionadded:: 1.3.5

        .. versionchanged:: 1.5.0
            Made as a function that returns :class:`User`.
        """
        id = int(self._payload.get("creator_id"))
        return self.http_client.fetch_user(id)

    def fetch_invited_users(self) -> Optional[List[User]]:
        """Fetches the invited users. Usually, users in this list are invited to speak via the Invite user option and have a Speaker role when the Space starts. Returns None if there isn't invited users.

        Returns
        ---------
        Optional[List[:class:`User`]]
            This method returns a list of users or an empty list if not found.


        .. versionadded:: 1.3.5

        .. versionchanged:: 1.5.0
            Made as a function that returns a list of :class:`User`.
        """
        if self._payload.get("invited_users"):
            ids = [int(id) for id in self._payload.get("invited_users")]
            return self.http_client.fetch_users(ids)
        return None

    def fetch_hosts(self) -> Optional[List[User]]:
        """Fetches the space's hosts.

        Returns
        ---------
        Optional[List[:class:`User`]]
            Returns a list of :class:`User`.


        .. versionadded:: 1.3.5

        .. versionchanged:: 1.5.0
            Made as a function that returns a list of :class:`User`.
        """
        if self._payload.get("host_ids"):
            ids = [int(id) for id in self._payload.get("host_ids")]
            return self.http_client.fetch_users(ids)
        return None

    def is_ticketed(self) -> bool:
        """An alias to :meth:`Space.ticketed`.

        Returns
        ---------
        :class:`bool`
            This method returns a :class:`bool` object.


        .. versionadded:: 1.3.5

        .. versionchanged:: 1.5.0
            Made as an alias to :meth:`Space.ticketed`.
        """
        return self.ticketed
