---
title: "How can I create proxies or alternative topologies?"
draft: false
---

Technically, proxies are pretty much the same things as clothes: They share file format and production pipeline.

To create a proxy, model it as full body clothing. See [[FAQ:How can I create clothes?]].

Once you have produced the "clothes" through MakeClothes, move the subdir that was created from "data/clothes/[my new item]" to "data/proxymeshes/[my new item]". Then rename the "[my new item].mhclo" file to "[my new item].proxy".

As a special notice: If you want existing skin textures to work with your proxy, you need to UV unwrap so that it fits upon an existing skin texture image.