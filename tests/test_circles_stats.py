from src.circles_stats import has_intersection, radius_sum

def test_two_intersections():
    c1 = {"x": 0, "y": 0, "r": 2}
    c2 = {"x": 3, "y": 0, "r": 2}
    assert has_intersection(c1, c2) == {"intersects": True, "intersections_count": 2}

def test_no_intersection_far():
    c1 = {"x": 0, "y": 0, "r": 1}
    c2 = {"x": 5, "y": 0, "r": 1}
    assert has_intersection(c1, c2) == {"intersects": False, "intersections_count": 0}

def test_external_tangent():
    c1 = {"x": 0, "y": 0, "r": 2}
    c2 = {"x": 4, "y": 0, "r": 2}
    assert has_intersection(c1, c2) == {"intersects": True, "intersections_count": 1}

def test_internal_tangent():
    c1 = {"x": 0, "y": 0, "r": 3}
    c2 = {"x": 1, "y": 0, "r": 2}
    assert has_intersection(c1, c2) == {"intersects": True, "intersections_count": 1}

def test_one_inside_other():
    c1 = {"x": 0, "y": 0, "r": 5}
    c2 = {"x": 1, "y": 1, "r": 1}
    assert has_intersection(c1, c2) == {"intersects": False, "intersections_count": 0}

def test_radius_sum():
    assert

git add .
git commit -m "Initial project structure, tests and README"
git branch -M main
git remote add origin <URL_TVEHO_REPOZITARE>
git push -u origin main
