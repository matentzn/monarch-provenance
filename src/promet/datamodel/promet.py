# Auto generated from promet.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-05-29T13:26:20
# Schema: promet
#
# id: https://w3id.org/monarchinitiative/promet
# description: A LinkML project for basic metadata for ontologies and datasets.
# license: BSD-3

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uri
from linkml_runtime.utils.metamodelcore import URI

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
DCAT = CurieNamespace('dcat', 'https://www.w3.org/ns/dcat#')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MONARCH_DATA = CurieNamespace('monarch_data', 'https://w3id.org/monarchinitiative/promet/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = MONARCH_DATA


# Types

# Class references
class NamedThingIdentifier(extended_str):
    pass


class EntityIdentifier(NamedThingIdentifier):
    pass


class ActivityIdentifier(NamedThingIdentifier):
    pass


class AgentIdentifier(NamedThingIdentifier):
    pass


class DatasetIdentifier(EntityIdentifier):
    pass


class DistributionIdentifier(EntityIdentifier):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = MONARCH_DATA.NamedThing

    identifier: Union[str, NamedThingIdentifier] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, NamedThingIdentifier):
            self.identifier = NamedThingIdentifier(self.identifier)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Entity(NamedThing):
    """
    An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real
    or imaginary [ref](https://www.w3.org/TR/prov-o/#Entity).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Entity"]
    class_class_curie: ClassVar[str] = "prov:Entity"
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = MONARCH_DATA.Entity

    identifier: Union[str, EntityIdentifier] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, EntityIdentifier):
            self.identifier = EntityIdentifier(self.identifier)

        super().__post_init__(**kwargs)


@dataclass
class Activity(NamedThing):
    """
    An activity is something that occurs over a period of time and acts upon or with entities; it may include
    consuming, processing, transforming, modifying, relocating, using, or generating entities
    [ref](https://www.w3.org/TR/prov-o/#Activity).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Activity"]
    class_class_curie: ClassVar[str] = "prov:Activity"
    class_name: ClassVar[str] = "Activity"
    class_model_uri: ClassVar[URIRef] = MONARCH_DATA.Activity

    identifier: Union[str, ActivityIdentifier] = None
    used: Optional[Union[str, EntityIdentifier]] = None
    attributed_to: Optional[Union[str, AgentIdentifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, ActivityIdentifier):
            self.identifier = ActivityIdentifier(self.identifier)

        if self.used is not None and not isinstance(self.used, EntityIdentifier):
            self.used = EntityIdentifier(self.used)

        if self.attributed_to is not None and not isinstance(self.attributed_to, AgentIdentifier):
            self.attributed_to = AgentIdentifier(self.attributed_to)

        super().__post_init__(**kwargs)


@dataclass
class Agent(NamedThing):
    """
    An agent is something that bears some form of responsibility for an activity taking place, for the existence of an
    entity, or for another agent's activity [ref](https://www.w3.org/TR/prov-o/#Agent).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PROV["Agent"]
    class_class_curie: ClassVar[str] = "prov:Agent"
    class_name: ClassVar[str] = "Agent"
    class_model_uri: ClassVar[URIRef] = MONARCH_DATA.Agent

    identifier: Union[str, AgentIdentifier] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, AgentIdentifier):
            self.identifier = AgentIdentifier(self.identifier)

        super().__post_init__(**kwargs)


@dataclass
class Dataset(Entity):
    """
    Represents a Dataset
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MONARCH_DATA["Dataset"]
    class_class_curie: ClassVar[str] = "monarch_data:Dataset"
    class_name: ClassVar[str] = "Dataset"
    class_model_uri: ClassVar[URIRef] = MONARCH_DATA.Dataset

    identifier: Union[str, DatasetIdentifier] = None
    title: Optional[str] = None
    description: Optional[str] = None
    issued: Optional[str] = None
    publisher: Optional[str] = None
    license: Optional[str] = None
    rights: Optional[str] = None
    version: Optional[str] = None
    contactPoint: Optional[str] = None
    distribution: Optional[Union[str, DistributionIdentifier]] = None
    generated_by: Optional[Union[str, ActivityIdentifier]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, DatasetIdentifier):
            self.identifier = DatasetIdentifier(self.identifier)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.issued is not None and not isinstance(self.issued, str):
            self.issued = str(self.issued)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.license is not None and not isinstance(self.license, str):
            self.license = str(self.license)

        if self.rights is not None and not isinstance(self.rights, str):
            self.rights = str(self.rights)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.contactPoint is not None and not isinstance(self.contactPoint, str):
            self.contactPoint = str(self.contactPoint)

        if self.distribution is not None and not isinstance(self.distribution, DistributionIdentifier):
            self.distribution = DistributionIdentifier(self.distribution)

        if self.generated_by is not None and not isinstance(self.generated_by, ActivityIdentifier):
            self.generated_by = ActivityIdentifier(self.generated_by)

        super().__post_init__(**kwargs)


@dataclass
class Distribution(Entity):
    """
    A specific representation of a dataset. A dataset might be available in multiple serializations that may differ in
    various ways, including natural language, media-type or format, schematic organization, temporal and spatial
    resolution, level of detail or profiles (which might specify any or all of the above)
    [ref](https://www.w3.org/TR/vocab-dcat-3/#Class:Distribution).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT["Distribution"]
    class_class_curie: ClassVar[str] = "dcat:Distribution"
    class_name: ClassVar[str] = "Distribution"
    class_model_uri: ClassVar[URIRef] = MONARCH_DATA.Distribution

    identifier: Union[str, DistributionIdentifier] = None
    title: Optional[str] = None
    accessURL: Optional[Union[str, URI]] = None
    downloadURL: Optional[Union[str, URI]] = None
    format: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.identifier):
            self.MissingRequiredField("identifier")
        if not isinstance(self.identifier, DistributionIdentifier):
            self.identifier = DistributionIdentifier(self.identifier)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.accessURL is not None and not isinstance(self.accessURL, URI):
            self.accessURL = URI(self.accessURL)

        if self.downloadURL is not None and not isinstance(self.downloadURL, URI):
            self.downloadURL = URI(self.downloadURL)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=MONARCH_DATA.name, domain=None, range=Optional[str])

slots.title = Slot(uri=DCTERMS.title, name="title", curie=DCTERMS.curie('title'),
                   model_uri=MONARCH_DATA.title, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=MONARCH_DATA.description, domain=None, range=Optional[str])

slots.identifier = Slot(uri=SCHEMA.identifier, name="identifier", curie=SCHEMA.curie('identifier'),
                   model_uri=MONARCH_DATA.identifier, domain=None, range=URIRef)

slots.issued = Slot(uri=DCTERMS.issued, name="issued", curie=DCTERMS.curie('issued'),
                   model_uri=MONARCH_DATA.issued, domain=None, range=Optional[str])

slots.publisher = Slot(uri=DCTERMS.publisher, name="publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=MONARCH_DATA.publisher, domain=None, range=Optional[str])

slots.license = Slot(uri=DCTERMS.license, name="license", curie=DCTERMS.curie('license'),
                   model_uri=MONARCH_DATA.license, domain=None, range=Optional[str])

slots.rights = Slot(uri=DCTERMS.rights, name="rights", curie=DCTERMS.curie('rights'),
                   model_uri=MONARCH_DATA.rights, domain=None, range=Optional[str])

slots.version = Slot(uri=DCAT.version, name="version", curie=DCAT.curie('version'),
                   model_uri=MONARCH_DATA.version, domain=None, range=Optional[str])

slots.contactPoint = Slot(uri=DCAT.contactPoint, name="contactPoint", curie=DCAT.curie('contactPoint'),
                   model_uri=MONARCH_DATA.contactPoint, domain=None, range=Optional[str])

slots.distribution = Slot(uri=DCAT.distribution, name="distribution", curie=DCAT.curie('distribution'),
                   model_uri=MONARCH_DATA.distribution, domain=None, range=Optional[Union[str, DistributionIdentifier]])

slots.accessURL = Slot(uri=DCAT.accessURL, name="accessURL", curie=DCAT.curie('accessURL'),
                   model_uri=MONARCH_DATA.accessURL, domain=None, range=Optional[Union[str, URI]])

slots.downloadURL = Slot(uri=DCAT.downloadURL, name="downloadURL", curie=DCAT.curie('downloadURL'),
                   model_uri=MONARCH_DATA.downloadURL, domain=None, range=Optional[Union[str, URI]])

slots.format = Slot(uri=DCTERMS.format, name="format", curie=DCTERMS.curie('format'),
                   model_uri=MONARCH_DATA.format, domain=None, range=Optional[str])

slots.generated_by = Slot(uri=PROV.wasGeneratedBy, name="generated_by", curie=PROV.curie('wasGeneratedBy'),
                   model_uri=MONARCH_DATA.generated_by, domain=None, range=Optional[Union[str, ActivityIdentifier]])

slots.used = Slot(uri=PROV.used, name="used", curie=PROV.curie('used'),
                   model_uri=MONARCH_DATA.used, domain=None, range=Optional[Union[str, EntityIdentifier]])

slots.attributed_to = Slot(uri=PROV.wasAttributedTo, name="attributed_to", curie=PROV.curie('wasAttributedTo'),
                   model_uri=MONARCH_DATA.attributed_to, domain=None, range=Optional[Union[str, AgentIdentifier]])