from ciphey.iface import Config
from ciphey.basemods.Crackers.xorcrypt import XorCrypt
cfg = Config().library_default().set_verbosity(3).complete_config()

ctext = [
    0x0a, 0x1d, 0x54, 0x0e, 0x02, 0x1a, 0x54, 0x0d, 0x0b, 0x0c, 0x54, 0x1d,
    0x0c, 0x1f, 0x11, 0x0b, 0x43, 0x1b, 0x1b, 0x18, 0x07, 0x49, 0x00, 0x11,
    0x02, 0x1d, 0x54, 0x15, 0x02, 0x10, 0x58, 0x59, 0x0c, 0x07, 0x54, 0x18,
    0x43, 0x0f, 0x06, 0x10, 0x07, 0x08, 0x0d, 0x59, 0x0d, 0x00, 0x13, 0x11,
    0x17, 0x49, 0x18, 0x18, 0x17, 0x0c, 0x54, 0x10, 0x0d, 0x49, 0x1a, 0x16,
    0x15, 0x0c, 0x19, 0x1b, 0x06, 0x1b, 0x58, 0x59, 0x01, 0x0c, 0x12, 0x16,
    0x11, 0x0c, 0x54, 0x0d, 0x0b, 0x0c, 0x54, 0x1f, 0x0a, 0x1b, 0x07, 0x0d,
    0x43, 0x06, 0x12, 0x59, 0x17, 0x01, 0x11, 0x59, 0x13, 0x0c, 0x06, 0x0a,
    0x0c, 0x07, 0x07, 0x59, 0x14, 0x00, 0x00, 0x11, 0x43, 0x1e, 0x1c, 0x16,
    0x0e, 0x49, 0x00, 0x11, 0x0a, 0x1a, 0x54, 0x11, 0x0a, 0x1a, 0x00, 0x16,
    0x11, 0x10, 0x54, 0x11, 0x02, 0x1a, 0x54, 0x1b, 0x16, 0x1a, 0x1d, 0x17,
    0x06, 0x1a, 0x07, 0x57
]

ctext = bytes(ctext)

print(ctext)

cfg.cache.mark_ctext(ctext)
cfg.cache.get_or_update(ctext, 0, lambda: 1)

res = XorCrypt(cfg).attemptCrack(ctext)

print(res)