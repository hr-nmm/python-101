from global_coordinates import GlobalCoordinates

nsp = GlobalCoordinates(latitude=(37, 46, 32.6, "N"), longitude=(122, 24, 39.4, "W"))
print(repr(nsp))  # <GlobalCoordinates lat=37°46'32.6"N lon=122°24'39.4"W>
print(
    f"No Starch Press's offices are at {nsp}"
)  # No Starch Press's offices are at 37°46'32.6"N 122°24'39.4"W>
print(str(nsp))  # 37°46'32.6"N 122°24'39.4"W>
nostarch = GlobalCoordinates(
    latitude=(37, 46, 32.6, "N"), longitude=(122, 24, 39.4, "W")
)

psf = GlobalCoordinates(latitude=(45, 27, 7.7, "N"), longitude=(122, 47, 30.2, "W"))

distance = nostarch(psf)
print(distance)  # 852.6857266443297
