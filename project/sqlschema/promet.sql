-- # Class: "NamedThing" Description: "A generic grouping for any identifiable entity."
--     * Slot: identifier Description: 
--     * Slot: name Description: 
--     * Slot: description Description: The description of the dataset.
-- # Class: "Entity" Description: "An entity is a physical, digital, conceptual, or other kind of thing with some fixed aspects; entities may be real or imaginary [ref](https://www.w3.org/TR/prov-o/#Entity)."
--     * Slot: identifier Description: 
--     * Slot: name Description: 
--     * Slot: description Description: The description of the dataset.
-- # Class: "Activity" Description: "An activity is something that occurs over a period of time and acts upon or with entities; it may include consuming, processing, transforming, modifying, relocating, using, or generating entities [ref](https://www.w3.org/TR/prov-o/#Activity)."
--     * Slot: used Description: 
--     * Slot: attributed_to Description: Attribution is the ascribing of an entity to an agent [ref](https://www.w3.org/TR/prov-o/#wasAttributedTo).
--     * Slot: identifier Description: 
--     * Slot: name Description: 
--     * Slot: description Description: The description of the dataset.
-- # Class: "Agent" Description: "An agent is something that bears some form of responsibility for an activity taking place, for the existence of an entity, or for another agent's activity [ref](https://www.w3.org/TR/prov-o/#Agent)."
--     * Slot: identifier Description: 
--     * Slot: name Description: 
--     * Slot: description Description: The description of the dataset.
-- # Class: "Dataset" Description: "Represents a Dataset"
--     * Slot: title Description: The title of the dataset.
--     * Slot: description Description: The description of the dataset.
--     * Slot: identifier Description: 
--     * Slot: issued Description: 
--     * Slot: publisher Description: 
--     * Slot: license Description: 
--     * Slot: rights Description: 
--     * Slot: version Description: 
--     * Slot: contactPoint Description: [ref](https://www.w3.org/TR/vocab-dcat-3/#Property:resource_contact_point).
--     * Slot: distribution Description: [ref](https://www.w3.org/TR/vocab-dcat-3/#Property:dataset_distribution)
--     * Slot: generated_by Description: 
--     * Slot: name Description: 
-- # Class: "Distribution" Description: "A specific representation of a dataset. A dataset might be available in multiple serializations that may differ in various ways, including natural language, media-type or format, schematic organization, temporal and spatial resolution, level of detail or profiles (which might specify any or all of the above) [ref](https://www.w3.org/TR/vocab-dcat-3/#Class:Distribution)."
--     * Slot: title Description: The title of the dataset.
--     * Slot: accessURL Description: 
--     * Slot: downloadURL Description: 
--     * Slot: format Description: The title of the dataset.
--     * Slot: identifier Description: 
--     * Slot: name Description: 
--     * Slot: description Description: The description of the dataset.

CREATE TABLE "NamedThing" (
	identifier TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (identifier)
);
CREATE TABLE "Entity" (
	identifier TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (identifier)
);
CREATE TABLE "Agent" (
	identifier TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (identifier)
);
CREATE TABLE "Distribution" (
	title TEXT, 
	"accessURL" TEXT, 
	"downloadURL" TEXT, 
	format TEXT, 
	identifier TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (identifier)
);
CREATE TABLE "Activity" (
	used TEXT, 
	attributed_to TEXT, 
	identifier TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (identifier), 
	FOREIGN KEY(used) REFERENCES "Entity" (identifier), 
	FOREIGN KEY(attributed_to) REFERENCES "Agent" (identifier)
);
CREATE TABLE "Dataset" (
	title TEXT, 
	description TEXT, 
	identifier TEXT NOT NULL, 
	issued TEXT, 
	publisher TEXT, 
	license TEXT, 
	rights TEXT, 
	version TEXT, 
	"contactPoint" TEXT, 
	distribution TEXT, 
	generated_by TEXT, 
	name TEXT, 
	PRIMARY KEY (identifier), 
	FOREIGN KEY(distribution) REFERENCES "Distribution" (identifier), 
	FOREIGN KEY(generated_by) REFERENCES "Activity" (identifier)
);