# AFDO_PROFILES maps a cc module name to a fully qualified fdo_profile module name
# AFDO_PROFILES is used to construct AfdoProfiles product var in Soong
# AFDO_PROFILES is applied to all products while PRODUCT_AFDO_PROFILES, which is set
# in a product config, has the ability to override it with custom profile
AFDO_PROFILES += keystore2://toolchain/pgo-profiles/sampling:keystore2 \
	libart://toolchain/pgo-profiles/sampling:libart \
	libartbase://toolchain/pgo-profiles/sampling:libartbase \
	libbinder://toolchain/pgo-profiles/sampling:libbinder \
	libbinder_ndk://toolchain/pgo-profiles/sampling:libbinder_ndk \
	libcrypto://toolchain/pgo-profiles/sampling:libcrypto \
	libgui://toolchain/pgo-profiles/sampling:libgui \
	libhidlbase://toolchain/pgo-profiles/sampling:libhidlbase \
	libhwui://toolchain/pgo-profiles/sampling:libhwui \
	libjpeg://toolchain/pgo-profiles/sampling:libjpeg \
	liblog://toolchain/pgo-profiles/sampling:liblog \
	libsensorservice://toolchain/pgo-profiles/sampling:libsensorservice \
	libsqlite://toolchain/pgo-profiles/sampling:libsqlite \
	libui://toolchain/pgo-profiles/sampling:libui \
	libutils://toolchain/pgo-profiles/sampling:libutils \
	libz://toolchain/pgo-profiles/sampling:libz \
	linker://toolchain/pgo-profiles/sampling:linker \
	lmkd://toolchain/pgo-profiles/sampling:lmkd \
	server_configurable_flags://toolchain/pgo-profiles/sampling:server_configurable_flags \
	surfaceflinger://toolchain/pgo-profiles/sampling:surfaceflinger
