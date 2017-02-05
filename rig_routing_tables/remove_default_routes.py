from rig.routing_table import MinimisationFailedError
from rig_routing_tables.utils import rig_to_c_table, c_to_rig_table
from _rig_routing_tables import lib


def minimise(table, target_length):
    """Minimise a Rig routing table by removing all entries which could be
    replaced by default routing.

    Parameters
    ----------
    routing_table : [:py:class:`~rig.routing_table.RoutingTableEntry`, ...]
        Routing table from which to remove entries which could be handled by
        default routing.
    target_length : int or None
        Target length of the routing table.

    Raises
    ------
    MinimisationFailedError
        If the smallest table that can be produced is larger than
        `target_length`.

    Returns
    -------
    [:py:class:`~rig.routing_table.RoutingTableEntry`, ...]
        Reduced routing table entries.
    """
    # Convert the table to C format and minimise
    c_table = rig_to_c_table(table)
    lib.remove_default_routes_minimise(c_table)

    # If the table is larger than the target length then raise an exception
    if target_length is not None and c_table.size > target_length:
        raise MinimisationFailedError(target_length, c_table.size)

    # Otherwise convert back to Rig form and return
    return c_to_rig_table(c_table)
