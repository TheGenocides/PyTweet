from typing import Any, Dict


class UserPublicMetrics:
    """Represent a PublicMetrics for a User.
    This PublicMetrics contain public info about the user.
    Version Added: 1.1.0

    Parameters:
    -----------
    data: Dict[str, Any]
        The complete data of the user's public metrics through a dictionary!

    Attributes:
    -----------
    original_payload
        Return the original payload of the user.

    _public
        Returns the user public metrics.
    """

    def __init__(self, data: Dict[str, Any] = {}, **kwargs: Any):
        self.original_payload = data
        self._public = self.original_payload.get("public_metrics")

    def __repr__(self) -> str:
        return f"UserPublicMetrics(user={self.original_payload.get('username')} followers_count={self.followers_count} following_count={self.following_count} tweet_count={self.tweet_count})"

    @property
    def followers_count(self) -> int:
        """int: Returns total of followers that a user has.
        Version Added:: 1.1.0
        """
        return int(self._public.get("followers_count"))

    @property
    def following_count(self) -> int:
        """int: Returns total of following that a user has.
        Version Added:: 1.1.0
        """
        return int(self._public.get("following_count"))

    @property
    def tweet_count(self) -> int:
        """int: Returns total of tweet that a user has.
        Version Added:: 1.1.0
        """
        return int(self._public.get("tweet_count"))

    @property
    def listed_count(self) -> int:
        """int: Returns total of listed that a user has.
        Version Added:: 1.1.0
        """
        return int(self._public.get("listed_count"))


class TweetPublicMetrics:
    """Represent a PublicMetrics for a tweet.
    This PublicMetrics contain public info about the tweet.
    Version Added: 1.1.0

    Parameters:
    -----------
    data: Dict[str, Any]:
        The complete data of the tweet's public metrics keep in a dictionary.

    Attributes:
    -----------
    original_payload
        Return the original payload of the tweet.

    _public
        Returns the user public metrics.
    """

    def __init__(self, data: Dict[str, Any] = {}, **kwargs: Any) -> None:
        self.original_payload = data
        self._public = data.get("public_metrics")

    def __repr__(self) -> str:
        return f"TweetPublicMetrics(like_count={self.like_count} retweet_count={self.retweet_count} reply_count={self.reply_count}> quote_count={self.quote_count})"

    @property
    def like_count(self) -> int:
        """int: Return total of likes that the tweet has.
        Version Added:: 1.1.0
        """
        return int(self._public.get("like_count"))

    @property
    def retweet_count(self) -> int:
        """int: Return total of retweetes that the tweet has.
        Version Added:: 1.1.0
        """
        return int(self._public.get("retweet_count"))

    @property
    def reply_count(self) -> int:
        """int: Return total of replies that the tweet has.
        Version Added:: 1.1.0
        """
        return int(self._public.get("reply_count"))

    @property
    def quote_count(self) -> int:
        """int: Return total of quotes that the tweet has.
        Version Added:: 1.1.0
        """
        return int(self._public.get("quote_count"))
