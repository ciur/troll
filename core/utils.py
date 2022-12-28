from .models import Node


def get_descendants(node_id, include_self=True):
    """Returns all descendants of the node"""
    sql = '''
    WITH RECURSIVE tree AS (
        SELECT * FROM core_node
          WHERE id = %s
        UNION ALL
        SELECT core_node.* FROM core_node, tree
          WHERE core_node.parent_id = tree.id
    )
    '''
    if include_self:
        sql += 'SELECT * FROM tree'
        return Node.objects.raw(sql, [node_id])

    sql += 'SELECT * FROM tree WHERE NOT id = %s'
    return Node.objects.raw(sql, [node_id, node_id])


def get_ancestors(node_id, include_self=True):
    """Returns all ancestors of the node"""
    sql = '''
    WITH RECURSIVE tree AS (
        SELECT * from core_node where id = %s
        UNION ALL
        SELECT core_node.*
            FROM core_node, tree WHERE core_node.id = tree.parent_id
    )
    '''
    if include_self:
        sql += 'SELECT * FROM tree'
        return Node.objects.raw(sql, [node_id])

    sql += 'SELECT * FROM tree WHERE NOT id = %s'

    return Node.objects.raw(sql, [node_id, node_id])
