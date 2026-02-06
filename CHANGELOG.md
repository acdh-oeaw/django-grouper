# Changelog

## [0.4.0](https://github.com/acdh-oeaw/django-grouper/compare/v0.3.0...v0.4.0) (2026-02-06)


### Features

* replace hardcoded merge functionality with signal ([101ad0f](https://github.com/acdh-oeaw/django-grouper/commit/101ad0fc907d075b3ce4a3e774bfe77ca4ae3a81))


### Bug Fixes

* **templates:** try different detail url routes ([976c411](https://github.com/acdh-oeaw/django-grouper/commit/976c4112af2edf6c2ebcfde7de3eab4bb6adc2b6))
* **templates:** update template for changed context_data ([29eb1ce](https://github.com/acdh-oeaw/django-grouper/commit/29eb1ce37d38478ae03fc185a34e7c92b0445446))
* **templates:** use select_template for base template ([3744b39](https://github.com/acdh-oeaw/django-grouper/commit/3744b3947b5e39f4f0a2330eff0596227048a2b6))


### Documentation

* **README:** add paragraph about the new `trigger_merge` signal ([345655f](https://github.com/acdh-oeaw/django-grouper/commit/345655f43c9fcc35b8c97e0941e40bb5dfba8203))

## [0.3.0](https://github.com/acdh-oeaw/django-grouper/compare/v0.2.0...v0.3.0) (2026-01-12)


### Features

* refactor grouping approach ([95c00d3](https://github.com/acdh-oeaw/django-grouper/commit/95c00d37f6b14c909d3fc9caa95163d5938f4d37))


### Documentation

* **README:** drop superfluous link from README ([26663f9](https://github.com/acdh-oeaw/django-grouper/commit/26663f90821b8aa1d63403109fd7352e597110dd))

## [0.2.0](https://github.com/acdh-oeaw/django-grouper/compare/v0.1.0...v0.2.0) (2024-08-28)


### Features

* add a info message that dissapears once a primary is selected ([0adecd6](https://github.com/acdh-oeaw/django-grouper/commit/0adecd6298292fda91c89a4de6253493ee141acf))
* allow to select one of the options as "primary" ([d7671bb](https://github.com/acdh-oeaw/django-grouper/commit/d7671bb8f14ff4ccf0d0db42c167072c9ac01ce6))
* change background of card on hover ([e3f4a89](https://github.com/acdh-oeaw/django-grouper/commit/e3f4a895893024e5f6d86268b5172f94829ea8e3))
* show preview of objects ([1c69b37](https://github.com/acdh-oeaw/django-grouper/commit/1c69b37d5502514c0a2d27df2e6ab875f9055115))
* style group listing ([39ffd74](https://github.com/acdh-oeaw/django-grouper/commit/39ffd7432b7ac71e4b5820a7760926d0fbe07c24))
* use diff.js to show the differences between the objects ([f8dd9da](https://github.com/acdh-oeaw/django-grouper/commit/f8dd9da4e1a05a63150bb9705d53276cb09e4a62))


### Bug Fixes

* make fundament footer margin bigger ([d7d80b3](https://github.com/acdh-oeaw/django-grouper/commit/d7d80b3a9337a30e505850f7ee53c4f4824dc9f3))
* make input as wide as card ([27601c6](https://github.com/acdh-oeaw/django-grouper/commit/27601c6f9370044baf48d60b2f0a96737c3466c3))
* replace details with pk in card title ([86f5255](https://github.com/acdh-oeaw/django-grouper/commit/86f5255af0d626c9aed1d0f3fb3f514f4636dcbc))
* **templates:** add missing slash ([fdd89ef](https://github.com/acdh-oeaw/django-grouper/commit/fdd89ef6b6c6d4afd112cbdbbb8303831bb83688))
* use the selected primary instead of creating a new object ([dcacbfc](https://github.com/acdh-oeaw/django-grouper/commit/dcacbfc439d71a6327a747e665b4825d69587a6b))

## 0.1.0 (2024-06-21)


### Features

* add group view to merge selected entities ([596cf47](https://github.com/acdh-oeaw/django-grouper/commit/596cf47505e894c4909aed27facb026367e7a475))
* allow to filter queryset before doing the grouping ([d02bbb9](https://github.com/acdh-oeaw/django-grouper/commit/d02bbb991748bcafda2d6fbed911bb156079d7e3))


### Documentation

* add changed information to README ([12d446e](https://github.com/acdh-oeaw/django-grouper/commit/12d446eca5d7e22220d2daa0a74f903d9246bb99))
