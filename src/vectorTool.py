"""
A Python module with functions to handle vectors.
"""
import numpy as np


def GetDistance(pt1, pt2) -> float:
    '''
    Return the length between two points.
    '''
    return sum(map(lambda ai, bi: (ai - bi)**2, pt1, pt2))**0.5


def GetOrient(pt1, pt2, unit='rad') -> float:
    '''
    Return the orientation defined by two points.
    Two types of angular unit are available including radian and degree.
    '''
    dx = pt2[0] - pt1[0]
    dy = pt2[1] - pt1[1]
    
    # Get quadrant
    if dx > 0 and dy >= 0:
        orient = np.arctan(dy/dx)
    elif dx < 0 and dy >= 0:
        orient = np.pi + np.arctan(dy/dx)
    elif dx < 0 and dy < 0:
        orient = np.pi + np.arctan(dy/dx)
    elif dx > 0 and dy < 0:
        orient = 2 * np.pi + np.arctan(dy/dx)
    elif dx == 0 and dy > 0:
        orient = 1 / 2 * np.pi
    elif dx == 0 and dy < 0:
        orient = 3 / 2 * np.pi
    elif dx == 0 and dy == 0:
        orient = 0

    # Unit
    if unit == 'rad':
        pass
    elif unit == 'deg':
        orient = np.degrees(orient)

    return orient


def MakeWithinTwoPi(direc) -> float:
    '''
    A recursive function that return a direction within 0 ~ 360 deg according to the argument.

    For example,
      723.1 >  363.1 >    3.1
    -1035.3 > -675.3 > -315.3 > 44.7
    
    '''
    direc = float(direc)

    nextStep=True

    if direc >= 360:
        direc -= 360

    elif direc < 0:
        direc += 360

    else:
        nextStep = False

    if nextStep == True:
        direc = MakeWithinTwoPi(direc)

    return direc


def NormalizeVector(vector) -> list:
    '''
    Return a normalized vector.
    '''
    length = sum([component**2 for component in vector])**0.5
    return [component/length for component in vector]


def TransCartesianSpheric(vector) -> list:
    '''
    Transform a vector from Cartesian coordinate system into spheric coordinate system.
    '''

    x, y, z = vector
    radius = (x**2 + y**2 + z**2)**0.5
    theta = np.arctan(y / (x**2 + z**2)**0.5)

    if x >= 0:
        phi = np.arctan(z/x)
    else:
        phi = np.arctan(z/x) + np.pi

    return [radius, theta, phi]


def TransCartesianPhi3(vector) -> list:
    '''
    Compute the rotational angles of a vector. Including phi1, phi2, phi3.
    phi1: rotation in YZ plane
    phi2: rotation in XZ plane
    phi3: rotation in XY plane
    '''
    x, y, z = vector
    radius = (x**2 + y**2 + z**2)**0.5

    phiList = [radius]
    for comp1, comp2 in ((y,z), (z,x), (x,y)):
        phi = GetOrient(comp1, comp2)
        phiList.append(phi)

    return phiList


def CheckTwoVectorOpposite(vec1, vec2) -> bool:
    '''
    If two vectors toward different directions, then True will be returned.
    Otherwise, the returned value will be False.
    '''
    len1 = GetDistance(vec1, (0, 0, 0))
    len2 = GetDistance(vec2, (0, 0, 0))

    innerProduct = np.dot(vec1, vec2)
    cosine = innerProduct/(len1*len2)

    if cosine > 0:
        opposite = False
    else:
        opposite = True
    
    return opposite


def GetAngleBetweenTwoVector(vec1, vec2, unit='rad') -> float:
    '''
    Compute the angle between two vectors.
    Two types of angular unit are available including radian and degree.
    '''
    len1 = GetDistance(vec1, (0, 0, 0))
    len2 = GetDistance(vec2, (0, 0, 0))

    innerProduct = np.dot(vec1, vec2)
    cosine = innerProduct/(len1*len2)
    cosine = round(cosine, 6) # prevent cosine = 1.00000000001
    
    if unit == 'rad':
        angle = np.arccos(cosine)
    elif unit == 'deg':
        angle = np.arccos(cosine) * 360 / (2*np.pi)
    else:
        raise Exception('Unknown unit')

    return angle


def GetPolygonArea(coords: np.ndarray) -> float:
    '''
    # Parameters

    coords: [[x0, y0], [x1, y1], ...]
    
    # Return

    area: float
    '''
    coords_2 = np.insert(coords[0:-1], 0, coords[-1], axis=0)
    area = abs(sum(coords[:, 0] * coords_2[:, 1] - coords[:, 1] * coords_2[:, 0])) / 2
    return area


if __name__ == '__main__':
    coords = np.array([[-1, -1], [-1, 0], [-1, 1], [1, 1], [1, -1]])
    area = GetPolygonArea(coords)
    print(area)

