# Minimal metadata for all Monarch related datasets

## Glossary

* _Dataset_: A collection of data, published or curated by a single agent, and available for access or download in one or more representations ([DCAT-3 spec](https://www.w3.org/TR/vocab-dcat-3/#Class:Dataset)). This includes, in particular:
    - Manually curated data, such as the HPO annotation files and the MAXO annotations 
    - Integrated datasets, such as knowledge graphs and knowledge graph components
    - Ontologies, such as HPO or Mondo.
    - Schemas, such as the SSSOM LinkML schema or the Phenopackets schema
    - SSSOM Mapping sets
    It is important to understand that a dataset is _independent of a specific serialisation, which we will refer to as a "distribution". It refers therefore to a logical rather than a concrete entity.
* _Distribution_: A specific representation of a dataset. A dataset might be available in multiple serializations that may differ in various ways, including natural language, media-type or format, schematic organization, temporal and spatial resolution, level of detail or profiles (which might specify any or all of the above) ([DCAT-3 spec](https://www.w3.org/TR/vocab-dcat-3/#Class:Distribution)). This includes, for example:
    - The KGX edges file of the Phenio KG in CSV format.
    - The Mondo disease mappings in SSSOM-TSV format.
    - The JSON serialisation of the "base-file" variant of the Mondo Disease Ontology.


## Common Practices

- [Practice 1: Every Monarch data artefact must have a PURL for download, metadata (including provenance) and documentation](#purl)

<a id="purl"></a>

### Practice 1: Every Monarch data artefact must have a PURL for download, metadata (including provenance) and documentation, eg

http://data.monarchinitiative.org/resources/phenio/distribution/phenio.owl
http://data.monarchinitiative.org/resources/phenio/documentation
http://data.monarchinitiative.org/resources/phenio/metadata

data.mi.org/resources/id # refers to a dataset
data.mi.org/resources/id/documentation
data.mi.org/resources/id/metadata

1. Every data publication process generates a provenance document which lists
    1. The process that generated the document with
        1. a versioned link to the data pipeline that was used to generate it, e.g. a makefile
        2. a versioned link to a documentation page that describes how the data is transformed
    2. The people and organisations attributed to the specific dataset
    3. The precise sources from which the dataset was derived (I think we should model source datasets ourselves)
2. Every automated data transformation or generation process (matching, prediction etc) generates a provenance file that describes the activities that led to the generation of the data, including derivation, attribution and generating process.
    1. In particular date
    2. incoming datasets
3. Other Manual efforts that do not fit in the above should 
    1. Be avoided (full automation)
    2. If not avoidable, lead to the documentation of the process at least on class level

For Mondo, we can easily implement a lot of the above in the ingest pipeline. We can potentially even map everything to the source field for now - it will be easy to switch this out later.

Every data product is associated with a provenance purl which has a JSON dump with provenance information. Every data product must be associated with a provenance purl.

Some of the release data sets could even contain their own metadata.

Right now we do not distinguish generating activity, attribution and derivation information in OBO format. 

Implement?

Automated processes should trace download URLs and Document these as part of provenance generation. (URL redirect chain). Ideally the version iri as well.

There is really no good way to start from a “latest” purl and get to a version iri in all cases. Every file should have a .metadata file associated with it with all important info?


Minimal Open Data metadata: https://centerforgov.gitbooks.io/open-data-metadata-guide/content/appendix-a.html#accessLevel


## Sources

- [Project Open Data metadata](https://centerforgov.gitbooks.io/open-data-metadata-guide/content/appendix-a.html): "The U.S. federal government has created the Project Open Data metadata schema standard to implement the federal open data policy. The Project Open Data schema is based on the international DCAT metadata schema used by open data programs around the world and has been mapped to many standards."
- [DCAT 3 Standard](https://www.w3.org/TR/vocab-dcat-3)
- [PROV Standard](https://www.w3.org/TR/prov-o/)
