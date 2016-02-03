from settings_common import *

MAX_NATIVE_ZOOM = 13

READ_ONLY_BASEDIR = True

# no CORS -- so don't use subdomains, or specify hostname (www.legacysurvey.org vs legacysurvey.org)
CAT_URL = '%s/{id}/{ver}/{z}/{x}/{y}.cat.json' % (ROOT_URL)

ENABLE_NEXP = False
ENABLE_VCC  = False
ENABLE_WL   = False
ENABLE_DR2  = True
ENABLE_DEPTH = False

#SDSS_PHOTOOBJS = '/project/projectdirs/cosmo/data/sdss/pre13/eboss/photoObj.v5b'

SDSS_PHOTOOBJS = '/project/projectdirs/cosmo/data/sdss/dr10/boss/photoObj'
SDSS_RESOLVE = '/project/projectdirs/cosmo/data/sdss/pre13/eboss/resolve/2013-07-29'

