---
title: "Norton Antivirus reports WS.Reputation.1 in the nightly build. What gives?"
draft: false
---

Norton Antivirus and other antivirus tools have a "feature" that classifies anything it doesn't recognize as a virus. A good discussion about this "feature" is available at http://community.norton.com/t5/Norton-Internet-Security-Norton/WS-Reputation-1-is-NOT-helpful/td-p/537550. Since the the development crew cannot spend money for a code signing certificate, there is now possibility to automatically whitelist MakeHuman.

The MakeHuman crew perceives this phenomenon as a bug with the antivirus solutions, and not with MakeHuman, and will refer any reports of the issue to the producer of the antivirus tool.

The suggested solution is to either switch the antivirus solution or to manually whitelist the binary on your local computer, under the precaution MakeHuman was received from a trusted source.