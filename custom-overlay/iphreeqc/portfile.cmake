vcpkg_check_linkage(ONLY_STATIC_LIBRARY)

vcpkg_from_github(
    OUT_SOURCE_PATH SOURCE_PATH
    REPO usgs-coupled/iphreeqc
    REF "tags/v${VERSION}"
    SHA512 e0deb97b536258c74411269394daba91a51dc4c00556029fd0edcbe021e5b751c546ade01e09f7c6227665313e8ba521e23aae969244feb4c6897c91ad473b22
    HEAD_REF master
)

vcpkg_cmake_configure(
    SOURCE_PATH "${SOURCE_PATH}"
    OPTIONS
        -DCMAKE_BUILD_TYPE=Release
        -DBUILD_TESTING=OFF
)

file(COPY "${SOURCE_PATH}/phreeqc3-doc/NOTICE.TXT" DESTINATION "${SOURCE_PATH}/doc/NOTICE")
file(WRITE "${SOURCE_PATH}/doc/README" "README\n")
file(WRITE "${SOURCE_PATH}/doc/RELEASE" "RELEASE\n")
file(WRITE "${SOURCE_PATH}/doc/html" "HTML\n")

vcpkg_cmake_install()