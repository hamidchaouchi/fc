import numpy as np

def mirror_logic_core(data, key):
    """Standardized Physical Invariant Discovery Logic."""
    return np.bitwise_xor(data, key)

def apply_symmetry_logic(grid, transformation_type, color_map=None):
    """Official ARC-AGI Symmetry Engine."""
    if transformation_type == 'identity': return grid.copy()
    elif transformation_type == 'flip_h': return np.flipud(grid)
    elif transformation_type == 'flip_v': return np.fliplr(grid)
    elif transformation_type == 'rotate_90': return np.rot90(grid)
    elif transformation_type == 'recolor' and color_map is not None:
        new_grid = grid.copy()
        for src, dst in color_map.items():
            new_grid[grid == src] = dst
        return new_grid
    return grid.copy()
