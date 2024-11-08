"""Various functions to deal with Beancount data."""

from __future__ import annotations

from typing import Any
from typing import TYPE_CHECKING

from beancount.core import compare  # type: ignore[attr-defined]
from beanquery import query  # type: ignore[import-untyped]
from beanquery import query_execute

if TYPE_CHECKING:  # pragma: no cover
    from typing import TypeAlias

    from fava.beans.abc import Directive
    from fava.beans.types import BeancountOptions

    class ResultType:
        """The Column type from beanquery (which has more attributes)."""

        name: str
        datatype: type[Any]

    ResultRow: TypeAlias = tuple[Any, ...]
    QueryResult: TypeAlias = tuple[list[ResultType], list[ResultRow]]


def hash_entry(entry: Directive) -> str:
    """Hash an entry."""
    if hasattr(entry, "_fields"):
        return compare.hash_entry(entry)  # type: ignore[no-any-return]
    return str(hash(entry))


def get_position(entry: Directive) -> tuple[str, int]:
    """Get the filename and position from the entry metadata."""
    meta = entry.meta
    filename = meta["filename"]
    lineno = meta["lineno"]
    if isinstance(filename, str) and isinstance(lineno, int):
        return (filename, lineno)
    msg = "Invalid filename or lineno in entry metadata."
    raise ValueError(msg)


def execute_query(query_: str) -> QueryResult:
    """Execture a query."""
    return query_execute.execute_query(  # type: ignore[no-any-return]
        query_
    )


def run_query(
    entries: list[Directive],
    options_map: BeancountOptions,
    _query: str,
    *,
    numberify: bool = False,
) -> QueryResult:
    """Run a query."""
    return query.run_query(  # type: ignore[no-any-return]
        entries,
        options_map,
        _query,
        numberify=numberify,
    )
