

CREATE TABLE "Agent" (
	identifier TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (identifier)
);

CREATE TABLE "Distribution" (
	identifier TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	title TEXT, 
	"accessURL" TEXT, 
	"downloadURL" TEXT, 
	format TEXT, 
	PRIMARY KEY (identifier)
);

CREATE TABLE "Entity" (
	identifier TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (identifier)
);

CREATE TABLE "NamedThing" (
	identifier TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (identifier)
);

CREATE TABLE "Activity" (
	identifier TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	used TEXT, 
	attributed_to TEXT, 
	PRIMARY KEY (identifier), 
	FOREIGN KEY(used) REFERENCES "Entity" (identifier), 
	FOREIGN KEY(attributed_to) REFERENCES "Agent" (identifier)
);

CREATE TABLE "Dataset" (
	name TEXT, 
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
	PRIMARY KEY (identifier), 
	FOREIGN KEY(distribution) REFERENCES "Distribution" (identifier), 
	FOREIGN KEY(generated_by) REFERENCES "Activity" (identifier)
);
