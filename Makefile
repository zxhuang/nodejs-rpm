usage:
	echo "Usage: make [node|download|rpm|clean]"

all: usage

#
# download node src tarball and rename
#
node_version_number=0.4.2
node_version=v$(node_version_number)
node_download_url=https://github.com/joyent/node/tarball/$(node_version)
local_tarball=node-$(node_version).tar.gz
node_dir=node-$(node_version)
download: clean
	wget --no-check-certificate $(node_download_url) -O $(local_tarball)
	tar zxvf $(local_tarball)
	mv joyent-node-* $(node_dir)
	tar zcvf $(node_dir).tar.gz $(node_dir)

#
# build nodejs rpm
#
rpmtop=noderpmbuild
node_rpm_spec=nodejs.spec
rpmtop_abs_path=`cd $(rpmtop); pwd`
rpm:
	-rm  -rf $(rpmtop)
	mkdir -p $(rpmtop)
	mkdir -p $(rpmtop)/{BUILD,SRPMS,RPMS,SPECS,SOURCES}
	mkdir -p $(rpmtop)/BUILD/usr/local/bin
	mkdir -p $(rpmtop)/BUILD/etc/rc.d/init.d
	mkdir -p $(rpmtop)/tmp
	cp $(node_dir).tar.gz $(rpmtop)/SOURCES/
	cp $(node_rpm_spec) $(rpmtop)/SPECS/
	rpmbuild --define="_tmppath $(rpmtop_abs_path)/tmp" --define="_topdir $(rpmtop_abs_path)" -ba $(node_rpm_spec)

clean:
	-rm -rf $(rpmtop) $(local_tarball) $(node_dir)

node: clean download rpm
