

def get_descendants(node_id, include_self=False):
    """Returns all descendants of the node"""
    """
    WITH RECURSIVE tree AS (
        SELECT * from core_node where id = %s
        UNION ALL
        SELECT core_node.*
            FROM core_node, tree WHERE node.id = tree.parent_id
    )
    SELECT * FROM tree NOT id = %s
    """
    pass


def get_ancestors(node_id, include_self=False):
    """Returns all ancestors of the node"""
    """
    WITH RECURSIVE tree AS (
        SELECT * from core_node where id = %s
        UNION ALL
        SELECT core_node.*
            FROM core_node, tree WHERE node.parent_id = tree.id
    )
    SELECT * FROM tree NOT id = %s
    """
    pass
