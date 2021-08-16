import numpy as np
import struct
from open3d import *


size_float = 4
list_pcd = []
with open("0000000001.bin", "rb") as f:
    byte = f.read(size_float * 4)
    while byte:
        x, y, z, intensity = struct.unpack("ffff", byte)
        list_pcd.append([x, y, z])
        byte = f.read(size_float * 4)
np_pcd = np.asarray(list_pcd)
pcd = PointCloud()
pcd.points = Vector3dVector(np_pcd)

open3d.io.write_point_cloud("copy_of_fragment.pcd", pcd)

