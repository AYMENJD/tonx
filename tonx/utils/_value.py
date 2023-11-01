import typing


def from_nanograms(value: int) -> float:
    """
    Converts from nanograms to toncoin

    Example:
        .. code-block:: python

            from_nano(1000000000)  # Returns 1.0

    Args:
        value (``int``):
            The value in nanograms to be converted

    Returns:
        :py:class:`float`:
            The converted value in toncoin
    """
    assert isinstance(value, (int, float))

    return value / 1e9


def to_nanograms(value: typing.Union[int, float]) -> int:
    """
    Converts a toncoin to nanograms

    Example:
        .. code-block:: python

            to_nano(1)  # Returns 1000000000

    Args:
        value (``int``):
            The value in toncoin to be converted

    Returns:
        :py:class:`int`:
            The converted value in nanograms
    """
    assert isinstance(value, (int, float))

    return int(value * 1e9)


def truncate_zeros(value: typing.Union[float, int]) -> typing.Union[float, int]:
    """
    Truncates trailing zeros from a number if it is a float

    Example:
        .. code-block:: python

            truncate_zeros(1.00)  # Returns 1
            truncate_zeros(1.05)  # Returns 1.05 (unchanged)

    Args:
        value (:py:class`int` || :py:class`float`):
            The number to be truncated

    Returns:
        :py:class`int` || :py:class`float`:
            The truncated number. If the input is a ``float`` and has no decimal places, it will be returned as an ``int``
            Otherwise, the input number will be returned as-is

    Raises:
        TypeError:
            If the input value is not a ``float`` or an ``int``
    """

    if isinstance(value, (float, int)):
        return int(value) if isinstance(value, float) and value.is_integer() else value

    raise TypeError("Value must be either float or int")
