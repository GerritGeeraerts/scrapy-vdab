# search endpoint
`POST https://www.vdab.be/rest/vindeenjob/v4/vacatureLight/zoek`
## [docs-endpoint-zoek.md](docs-endpoint-zoek.md)POST Data:
```json
  {
     "criteria": {
        "arbeidsduurCodes": [],
        "arbeidsregimeCodes": [],
        "attestCodes": [],
        "beroepCodes": [],
        "contractTypeCodes": [],
        "diplomaCodes": [],
        "ervaringCodes": [],
        "internationaalCodes": [],
        "jobdomeinCodes": [],
        "locatieCriteria": {
           "geoLocatie": {
              "latitude": null,
              "longitude": null
           },
           "locatieCode": "2643",
           "locatiePostcodeGemeente": "9451 Kerksken",
           "straalInKilometer": 30
        },
        "onlineSindsCode": "9000",
        "rijbewijsCodes": [],
        "sorteerVeld": "DATUM",
        "taalCriteria": {
           "taalSelecties": []
        },
        "trefwoord": {search_query}
     },
     "pagina": {pagina},
     "paginaGrootte": 15,
     "zoekmodus": "C2"
  }
```
## Response data example:
```json
  {
     "filters": {
        "arbeidsduur": [
           {
              "aantalResultaten": 3,
              "code": "D",
              "omschrijving": "Deeltijds"
           },
           {
              "aantalResultaten": 854,
              "code": "V",
              "omschrijving": "Voltijds"
           }
        ],
        "arbeidsregime": [
           {
              "aantalResultaten": 854,
              "code": "D",
              "omschrijving": "Dagwerk"
           },
           {
              "aantalResultaten": 3,
              "code": "2",
              "omschrijving": "2-ploegenstelsel"
           },
           {
              "aantalResultaten": 1,
              "code": "Z",
              "omschrijving": "Weekendwerk"
           },
           {
              "aantalResultaten": 1,
              "code": "V",
              "omschrijving": "Volcontinu systeem"
           }
        ],
        "beroep": [
           {
              "aantalResultaten": 99,
              "code": "263af849-d6f5-425b-9eb9-41aefc558f96",
              "omschrijving": "Software ontwikkelaar"
           },
           {
              "aantalResultaten": 66,
              "code": "ac2e8fda-9440-4d7e-932c-5a9891cdb958",
              "omschrijving": "Data engineer"
           },
           {
              "aantalResultaten": 64,
              "code": "2a0d6ea6-0de3-452d-aa93-7e575a593254",
              "omschrijving": "Support medewerker ICT"
           },
           {
              "aantalResultaten": 62,
              "code": "9f40e4a2-47a2-48bd-aa0c-cc9bda6c9d58",
              "omschrijving": "Systeembeheerder"
           },
           {
              "aantalResultaten": 53,
              "code": "97af1203-2341-46d1-9ca9-b00b7284062a",
              "omschrijving": "Expert productieproces en -methodes"
           },
           {
              "aantalResultaten": 37,
              "code": "47c71e40-3fca-43db-9eb6-289c2f216105",
              "omschrijving": "Data manager"
           },
           {
              "aantalResultaten": 37,
              "code": "6b21d54c-49b7-44cb-81c9-a4bb3cd88b96",
              "omschrijving": "Integratie expert ICT"
           },
           {
              "aantalResultaten": 29,
              "code": "3d87a629-d78d-4fee-8597-3b5daf475447",
              "omschrijving": "Verantwoordelijke kwaliteitscontrole"
           },
           {
              "aantalResultaten": 29,
              "code": "b61d0f71-273f-4134-831f-bd80e6bd15b3",
              "omschrijving": "Productieplanner"
           },
           {
              "aantalResultaten": 25,
              "code": "f8e6669d-db4d-4ddb-a31a-26e55bfeaaf9",
              "omschrijving": "Ontwerper industriële automatisering"
           },
           {
              "aantalResultaten": 21,
              "code": "eccbc68a-353d-40a7-85aa-6577457b3218",
              "omschrijving": "Aankoper"
           },
           {
              "aantalResultaten": 18,
              "code": "acfddd4d-cc1e-419e-a369-974fb5a37ccd",
              "omschrijving": "Data scientist"
           },
           {
              "aantalResultaten": 15,
              "code": "c9014baf-c35c-4abe-81a0-27e3b6e6ac1b",
              "omschrijving": "Software analist"
           },
           {
              "aantalResultaten": 13,
              "code": "48e6a6d9-0699-4eff-8cb2-6eb980fda706",
              "omschrijving": "Verantwoordelijke industrieel onderhoud"
           },
           {
              "aantalResultaten": 12,
              "code": "06d059a3-6f65-4b4f-b359-8a27ce3c3594",
              "omschrijving": "Logistiek verantwoordelijke"
           },
           {
              "aantalResultaten": 12,
              "code": "410a4483-7305-496a-93f2-613e6e5930fd",
              "omschrijving": "Industrieel onderhoudstechnicus"
           },
           {
              "aantalResultaten": 12,
              "code": "d70607ef-e4cf-43a9-a340-a1b9e9d8e3f9",
              "omschrijving": "Polyvalent administratief medewerker"
           },
           {
              "aantalResultaten": 11,
              "code": "92f4b097-c6d3-47cf-bb9c-5193e0ab1853",
              "omschrijving": "Projectmanager engineering"
           },
           {
              "aantalResultaten": 11,
              "code": "de070231-7a9f-4a83-9604-669ca3837bd6",
              "omschrijving": "Verantwoordelijke productieproces en -methodes"
           },
           {
              "aantalResultaten": 10,
              "code": "4da1e783-4d2b-45b2-b213-113c8ef342ff",
              "omschrijving": "Sales engineer"
           },
           {
              "aantalResultaten": 10,
              "code": "54a6cf77-d3ff-4691-b03d-f9e30b4790ef",
              "omschrijving": "Vertegenwoordiger B2B"
           },
           {
              "aantalResultaten": 10,
              "code": "7d63beb9-03ad-44e9-a77b-c02f2c28ebc0",
              "omschrijving": "Landmeter"
           },
           {
              "aantalResultaten": 9,
              "code": "7396864b-9eaf-440f-a285-ef793f9785da",
              "omschrijving": "Technisch-administratief medewerker"
           },
           {
              "aantalResultaten": 8,
              "code": "0e20e520-a445-4866-8666-3e0ee9706b4c",
              "omschrijving": "Verantwoordelijke ICT"
           },
           {
              "aantalResultaten": 8,
              "code": "237e4c85-b9a0-48da-a112-3724d479dae8",
              "omschrijving": "Tekenaar-ontwerper elektriciteit, elektronica"
           },
           {
              "aantalResultaten": 8,
              "code": "88cbf041-02e1-432e-9d49-c1a2c20c5784",
              "omschrijving": "Medewerker communicatie"
           },
           {
              "aantalResultaten": 8,
              "code": "e09de2fb-b2bc-4feb-8c78-065dc319c3ae",
              "omschrijving": "Werkvoorbereider"
           },
           {
              "aantalResultaten": 7,
              "code": "397c9e4c-7dc9-4b3c-93c2-6f79a6b98c4a",
              "omschrijving": "Netwerkbeheerder"
           },
           {
              "aantalResultaten": 7,
              "code": "70dce6b8-8a32-4993-ac2d-cef19c773ccd",
              "omschrijving": "ICT architect"
           },
           {
              "aantalResultaten": 7,
              "code": "cfe84de1-a7d1-4b34-924d-764c2cb3c649",
              "omschrijving": "Elektrotechnicus"
           }
        ],
        "contractTypes": [
           {
              "aantalResultaten": 726,
              "code": "8",
              "omschrijving": "Vaste jobs"
           },
           {
              "aantalResultaten": 32,
              "code": "4",
              "omschrijving": "Tijdelijke jobs"
           },
           {
              "aantalResultaten": 66,
              "code": "5",
              "omschrijving": "Tijdelijke jobs met optie vast"
           },
           {
              "aantalResultaten": 1,
              "code": "2",
              "omschrijving": "Tewerkstellingsmaatregelen"
           },
           {
              "aantalResultaten": 32,
              "code": "10",
              "omschrijving": "Zelfstandige activiteit"
           }
        ],
        "diploma": [
           {
              "aantalResultaten": 56,
              "code": "A",
              "omschrijving": "Geen"
           },
           {
              "aantalResultaten": 14,
              "code": "B",
              "omschrijving": "Lager onderwijs"
           },
           {
              "aantalResultaten": 87,
              "code": "C",
              "omschrijving": "Secundair onderwijs"
           },
           {
              "aantalResultaten": 31,
              "code": "F",
              "omschrijving": "Graduaat/HBO5"
           },
           {
              "aantalResultaten": 564,
              "code": "D",
              "omschrijving": "Bachelor"
           },
           {
              "aantalResultaten": 337,
              "code": "E",
              "omschrijving": "Master"
           }
        ],
        "ervaring": [
           {
              "aantalResultaten": 3,
              "code": "0",
              "omschrijving": "Niet van belang"
           },
           {
              "aantalResultaten": 182,
              "code": "1",
              "omschrijving": "Geen ervaring"
           },
           {
              "aantalResultaten": 148,
              "code": "2",
              "omschrijving": "Beperkte ervaring"
           },
           {
              "aantalResultaten": 366,
              "code": "3",
              "omschrijving": "Minstens 2 jaar ervaring"
           },
           {
              "aantalResultaten": 154,
              "code": "4",
              "omschrijving": "Minstens 5 jaar ervaring"
           }
        ],
        "internationaal": [],
        "jobdomein": [
           {
              "aantalResultaten": 20,
              "code": "JOBCAT01",
              "omschrijving": "Aankoop"
           },
           {
              "aantalResultaten": 53,
              "code": "JOBCAT02",
              "omschrijving": "Administratie"
           },
           {
              "aantalResultaten": 36,
              "code": "JOBCAT03",
              "omschrijving": "Bouw"
           },
           {
              "aantalResultaten": 11,
              "code": "JOBCAT04",
              "omschrijving": "Communicatie"
           },
           {
              "aantalResultaten": 2,
              "code": "JOBCAT05",
              "omschrijving": "Creatief"
           },
           {
              "aantalResultaten": 14,
              "code": "JOBCAT14",
              "omschrijving": "Dienstverlening"
           },
           {
              "aantalResultaten": 7,
              "code": "JOBCAT06",
              "omschrijving": "Financieel"
           },
           {
              "aantalResultaten": 1,
              "code": "JOBCAT07",
              "omschrijving": "Gezondheid"
           },
           {
              "aantalResultaten": 1,
              "code": "JOBCAT08",
              "omschrijving": "Horeca en toerisme"
           },
           {
              "aantalResultaten": 11,
              "code": "JOBCAT09",
              "omschrijving": "Human resources"
           },
           {
              "aantalResultaten": 422,
              "code": "JOBCAT10",
              "omschrijving": "ICT"
           },
           {
              "aantalResultaten": 4,
              "code": "JOBCAT11",
              "omschrijving": "Juridisch"
           },
           {
              "aantalResultaten": 2,
              "code": "JOBCAT12",
              "omschrijving": "Land- en tuinbouw"
           },
           {
              "aantalResultaten": 35,
              "code": "JOBCAT13",
              "omschrijving": "Logistiek en transport"
           },
           {
              "aantalResultaten": 56,
              "code": "JOBCAT15",
              "omschrijving": "Management"
           },
           {
              "aantalResultaten": 11,
              "code": "JOBCAT16",
              "omschrijving": "Marketing"
           },
           {
              "aantalResultaten": 1,
              "code": "JOBCAT17",
              "omschrijving": "Onderhoud"
           },
           {
              "aantalResultaten": 2,
              "code": "JOBCAT18",
              "omschrijving": "Onderwijs"
           },
           {
              "aantalResultaten": 42,
              "code": "JOBCAT20",
              "omschrijving": "Onderzoek en ontwikkeling"
           },
           {
              "aantalResultaten": 14,
              "code": "JOBCAT19",
              "omschrijving": "Overheid"
           },
           {
              "aantalResultaten": 27,
              "code": "JOBCAT21",
              "omschrijving": "Productie"
           },
           {
              "aantalResultaten": 289,
              "code": "JOBCAT22",
              "omschrijving": "Techniek"
           },
           {
              "aantalResultaten": 21,
              "code": "JOBCAT23",
              "omschrijving": "Verkoop"
           },
           {
              "aantalResultaten": 19,
              "code": "JOBCAT24",
              "omschrijving": "Andere"
           }
        ],
        "onlineSinds": [
           {
              "aantalResultaten": 26,
              "code": "1",
              "omschrijving": "Vandaag of gisteren"
           },
           {
              "aantalResultaten": 137,
              "code": "6",
              "omschrijving": "Voorbije week"
           },
           {
              "aantalResultaten": 857,
              "code": "9000",
              "omschrijving": "Alle jobs"
           }
        ],
        "rijbewijs": [
           {
              "aantalResultaten": 731,
              "code": "0",
              "omschrijving": "Geen rijbewijs"
           },
           {
              "aantalResultaten": 124,
              "code": "B",
              "omschrijving": "Auto's <. 3,5t en max. 8 plaatsen"
           },
           {
              "aantalResultaten": 2,
              "code": "BE",
              "omschrijving": "Auto's < 3,5t en max. 8 plaatsen met aanhangwagen htm > 750 kg"
           }
        ],
        "taalniveaus": [
           {
              "aantalResultaten": 0,
              "code": "10",
              "omschrijving": "Geen"
           },
           {
              "aantalResultaten": 0,
              "code": "11",
              "omschrijving": "Starter"
           },
           {
              "aantalResultaten": 0,
              "code": "12",
              "omschrijving": "Basis"
           },
           {
              "aantalResultaten": 0,
              "code": "13",
              "omschrijving": "Medium"
           },
           {
              "aantalResultaten": 0,
              "code": "14",
              "omschrijving": "Goed"
           },
           {
              "aantalResultaten": 0,
              "code": "15",
              "omschrijving": "Zeer goed"
           }
        ]
     },
     "pagina": 1,
     "paginaGrootte": 15,
     "resultaten": [
        {
           "aantalJobs": 1,
           "dubbels": [],
           "eerstePublicatieDatum": "2025-08-30T03:08:02Z",
           "gesloten": false,
           "id": {
              "id": 71829072
           },
           "laatsteWijzigingDatum": "2025-08-30T03:08:02Z",
           "leverancier": {
              "bedrijvenGalerijId": 3777,
              "gemandateerd": true,
              "type": "GEWONE_BEDRIJVEN"
           },
           "locatie": {},
           "opmaak": {
              "altText": "Logo Maandag Belgium",
              "logo": "https://cdn.app-prd-cdn.aws.vdab-prd.be/vindeenjob/templates/bedrijven/3777/mobileLogo.png"
           },
           "tewerkstellingsLocatieRegioOfAdres": "ANTWERPEN",
           "vacatureBedrijfsnaam": "Maandag Belgium",
           "vacaturefunctie": {
              "arbeidscircuitLijn": "Vaste Job",
              "naam": "Artwork & BOM Coördinator"
           }
        },
        {
           "aantalJobs": 1,
           "dubbels": [],
           "eerstePublicatieDatum": "2025-08-29T12:03:24Z",
           "gesloten": false,
           "id": {
              "id": 71822945
           },
           "laatsteWijzigingDatum": "2025-08-29T12:03:24Z",
           "leverancier": {
              "bedrijvenGalerijId": 3845,
              "gemandateerd": true,
              "type": "INTERMEDIAIREN"
           },
           "locatie": {},
           "opmaak": {
              "altText": "Logo Synergie Belgium",
              "logo": "https://cdn.app-prd-cdn.aws.vdab-prd.be/vindeenjob/templates/bedrijven/3845/mobileLogo.png"
           },
           "tewerkstellingsLocatieRegioOfAdres": "BEVEREN-KRUIBEKE-ZWIJNDRECHT",
           "vacatureBedrijfsnaam": "Synergie Waaslandhaven Interim",
           "vacaturefunctie": {
              "arbeidscircuitLijn": "Interim met optie \"vast werk\"",
              "naam": "Data-analist Engineer"
           }
        },
        {
           "aantalJobs": 1,
           "dubbels": [],
           "eerstePublicatieDatum": "2025-08-29T16:12:34Z",
           "gesloten": false,
           "id": {
              "id": 71826940
           },
           "laatsteWijzigingDatum": "2025-08-29T16:12:34Z",
           "leverancier": {
              "gemandateerd": true,
              "type": "GEWONE_BEDRIJVEN"
           },
           "locatie": {},
           "tewerkstellingsLocatieRegioOfAdres": "GENT",
           "vacatureBedrijfsnaam": "Rekruut",
           "vacaturefunctie": {
              "arbeidscircuitLijn": "Vaste Job",
              "naam": "Customer Support Engineer"
           }
        },
        {
           "aantalJobs": 1,
           "dubbels": [],
           "eerstePublicatieDatum": "2025-08-29T16:11:30Z",
           "gesloten": false,
           "id": {
              "id": 71826925
           },
           "laatsteWijzigingDatum": "2025-08-29T16:11:30Z",
           "leverancier": {
              "gemandateerd": true,
              "type": "GEWONE_BEDRIJVEN"
           },
           "locatie": {},
           "tewerkstellingsLocatieRegioOfAdres": "BRUSSEL",
           "vacatureBedrijfsnaam": "Rekruut",
           "vacaturefunctie": {
              "arbeidscircuitLijn": "Vaste Job",
              "naam": "Senior Python Engineer"
           }
        },
        {
           "aantalJobs": 1,
           "dubbels": [],
           "eerstePublicatieDatum": "2025-08-29T15:54:17Z",
           "gesloten": false,
           "id": {
              "id": 71826585
           },
           "laatsteWijzigingDatum": "2025-08-29T15:54:17Z",
           "leverancier": {
              "bedrijvenGalerijId": 4958,
              "gemandateerd": true,
              "type": "INTERMEDIAIREN"
           },
           "locatie": {},
           "opmaak": {
              "altText": "Logo Wolfson Recruitment",
              "logo": "https://cdn.app-prd-cdn.aws.vdab-prd.be/vindeenjob/templates/bedrijven/4958/mobileLogo.png"
           },
           "tewerkstellingsLocatieRegioOfAdres": "GENT",
           "vacatureBedrijfsnaam": "Wolfson Recruitment",
           "vacaturefunctie": {
              "arbeidscircuitLijn": "Vaste Job",
              "naam": "Reliability Engineer - Maakindustrie"
           }
        },
        {
           "aantalJobs": 1,
           "dubbels": [],
           "eerstePublicatieDatum": "2025-08-29T16:41:25Z",
           "gesloten": false,
           "id": {
              "id": 71827350
           },
           "laatsteWijzigingDatum": "2025-08-29T16:41:25Z",
           "leverancier": {
              "bedrijvenGalerijId": 4151,
              "gemandateerd": true,
              "type": "DERDENLEVERANCIERS"
           },
           "locatie": {},
           "opmaak": {
              "altText": "Logo Editx",
              "logo": "https://cdn.app-prd-cdn.aws.vdab-prd.be/vindeenjob/templates/bedrijven/4151/mobileLogo.png"
           },
           "tewerkstellingsLocatieRegioOfAdres": "MERELBEKE-MELLE",
           "vacatureBedrijfsnaam": "Pauwels Consulting",
           "vacaturefunctie": {
              "arbeidscircuitLijn": "Tijdelijke job (niet via uitzendkantoren)",
              "naam": "Data & BI consultant (Azure / Databricks / Power BI)"
           }
        },
        {
           "aantalJobs": 1,
           "dubbels": [],
           "eerstePublicatieDatum": "2025-08-29T15:51:52Z",
           "gesloten": false,
           "id": {
              "id": 71826542
           },
           "laatsteWijzigingDatum": "2025-08-29T15:51:52Z",
           "leverancier": {
              "bedrijvenGalerijId": 4958,
              "gemandateerd": true,
              "type": "INTERMEDIAIREN"
           },
           "locatie": {},
           "opmaak": {
              "altText": "Logo Wolfson Recruitment",
              "logo": "https://cdn.app-prd-cdn.aws.vdab-prd.be/vindeenjob/templates/bedrijven/4958/mobileLogo.png"
           },
           "tewerkstellingsLocatieRegioOfAdres": "BAVIKHOVE",
           "vacatureBedrijfsnaam": "Wolfson Recruitment",
           "vacaturefunctie": {
              "arbeidscircuitLijn": "Vaste Job",
              "naam": "Ai Automation Engineer"
           }
        },
        {
           "aantalJobs": 1,
           "dubbels": [],
           "eerstePublicatieDatum": "2025-08-29T03:08:22Z",
           "gesloten": false,
           "id": {
              "id": 71819038
           },
           "laatsteWijzigingDatum": "2025-08-29T03:08:22Z",
           "leverancier": {
              "bedrijvenGalerijId": 3777,
              "gemandateerd": true,
              "type": "GEWONE_BEDRIJVEN"
           },
           "locatie": {},
           "opmaak": {
              "altText": "Logo Maandag Belgium",
              "logo": "https://cdn.app-prd-cdn.aws.vdab-prd.be/vindeenjob/templates/bedrijven/3777/mobileLogo.png"
           },
           "tewerkstellingsLocatieRegioOfAdres": "ANTWERPEN",
           "vacatureBedrijfsnaam": "Maandag Belgium",
           "vacaturefunctie": {
              "arbeidscircuitLijn": "Vaste Job",
              "naam": "Project Engineer Masterbatch Records"
           }
        },
        {
           "aantalJobs": 1,
           "dubbels": [],
           "eerstePublicatieDatum": "2025-08-29T03:31:59Z",
           "gesloten": false,
           "id": {
              "id": 71819061
           },
           "laatsteWijzigingDatum": "2025-08-29T03:31:59Z",
           "leverancier": {
              "bedrijvenGalerijId": 3769,
              "gemandateerd": true,
              "type": "DERDENLEVERANCIERS"
           },
           "locatie": {},
           "opmaak": {
              "altText": "Logo Jobat",
              "logo": "https://cdn.app-prd-cdn.aws.vdab-prd.be/vindeenjob/templates/bedrijven/3769/mobileLogo.jpg"
           },
           "tewerkstellingsLocatieRegioOfAdres": "SINT-GILLIS",
           "vacatureBedrijfsnaam": "VIVALDIS - HK",
           "vacaturefunctie": {
              "arbeidscircuitLijn": "Vaste Job",
              "naam": "Development Engineer Medior"
           }
        },
        {
           "aantalJobs": 1,
           "dubbels": [],
           "eerstePublicatieDatum": "2025-08-29T00:05:05Z",
           "gesloten": false,
           "id": {
              "id": 71818701
           },
           "laatsteWijzigingDatum": "2025-08-29T00:05:05Z",
           "leverancier": {
              "bedrijvenGalerijId": 3790,
              "gemandateerd": true,
              "type": "INTERMEDIAIREN"
           },
           "locatie": {},
           "opmaak": {
              "altText": "Logo Talentus",
              "logo": "https://cdn.app-prd-cdn.aws.vdab-prd.be/vindeenjob/templates/bedrijven/3790/mobileLogo.png"
           },
           "tewerkstellingsLocatieRegioOfAdres": "TIELT",
           "vacatureBedrijfsnaam": "Talentus",
           "vacaturefunctie": {
              "arbeidscircuitLijn": "Vaste Job",
              "naam": "Operational Excellence engineer"
           }
        },
        {
           "aantalJobs": 1,
           "dubbels": [],
           "eerstePublicatieDatum": "2025-08-29T15:59:00Z",
           "gesloten": false,
           "id": {
              "id": 71826715
           },
           "laatsteWijzigingDatum": "2025-08-29T15:59:00Z",
           "leverancier": {
              "bedrijvenGalerijId": 4642,
              "gemandateerd": true,
              "type": "INTERMEDIAIREN"
           },
           "locatie": {},
           "opmaak": {
              "altText": "Logo Faktor",
              "logo": "https://cdn.app-prd-cdn.aws.vdab-prd.be/vindeenjob/templates/bedrijven/4642/mobileLogo.png"
           },
           "tewerkstellingsLocatieRegioOfAdres": "TIELT",
           "vacatureBedrijfsnaam": "Faktor",
           "vacaturefunctie": {
              "arbeidscircuitLijn": "Vaste Job",
              "naam": "Continuous Improvement Engineer"
           }
        },
        {
           "aantalJobs": 1,
           "dubbels": [],
           "eerstePublicatieDatum": "2025-08-29T09:34:02Z",
           "gesloten": false,
           "id": {
              "id": 71820655
           },
           "laatsteWijzigingDatum": "2025-08-29T09:34:02Z",
           "leverancier": {
              "bedrijvenGalerijId": 4151,
              "gemandateerd": true,
              "type": "DERDENLEVERANCIERS"
           },
           "locatie": {},
           "opmaak": {
              "altText": "Logo Editx",
              "logo": "https://cdn.app-prd-cdn.aws.vdab-prd.be/vindeenjob/templates/bedrijven/4151/mobileLogo.png"
           },
           "tewerkstellingsLocatieRegioOfAdres": "ZAVENTEM",
           "vacatureBedrijfsnaam": "TMC Belgium",
           "vacaturefunctie": {
              "arbeidscircuitLijn": "Zelfstandige activiteit",
              "naam": "Junior Network Engineer"
           }
        },
        {
           "aantalJobs": 1,
           "dubbels": [],
           "eerstePublicatieDatum": "2025-08-29T17:38:08Z",
           "gesloten": false,
           "id": {
              "id": 71828012
           },
           "laatsteWijzigingDatum": "2025-08-29T17:38:08Z",
           "leverancier": {
              "bedrijvenGalerijId": 4151,
              "gemandateerd": true,
              "type": "DERDENLEVERANCIERS"
           },
           "locatie": {},
           "opmaak": {
              "altText": "Logo Editx",
              "logo": "https://cdn.app-prd-cdn.aws.vdab-prd.be/vindeenjob/templates/bedrijven/4151/mobileLogo.png"
           },
           "tewerkstellingsLocatieRegioOfAdres": "OUDERGEM",
           "vacatureBedrijfsnaam": "Sander",
           "vacaturefunctie": {
              "arbeidscircuitLijn": "Vaste Job",
              "naam": "Senior System Engineer | Aviation"
           }
        },
        {
           "aantalJobs": 1,
           "dubbels": [],
           "eerstePublicatieDatum": "2025-08-29T08:18:18Z",
           "gesloten": false,
           "id": {
              "id": 71820097
           },
           "laatsteWijzigingDatum": "2025-08-29T08:18:18Z",
           "leverancier": {
              "bedrijvenGalerijId": 3041,
              "gemandateerd": true,
              "type": "INTERMEDIAIREN"
           },
           "locatie": {},
           "opmaak": {
              "altText": "Logo Vivaldis Interim",
              "logo": "https://cdn.app-prd-cdn.aws.vdab-prd.be/vindeenjob/templates/bedrijven/3041/mobileLogo.jpg"
           },
           "tewerkstellingsLocatieRegioOfAdres": "BISSEGEM",
           "vacatureBedrijfsnaam": "Vivaldis Interim",
           "vacaturefunctie": {
              "arbeidscircuitLijn": "Interim met optie \"vast werk\"",
              "naam": "productiemanager glas"
           }
        },
        {
           "aantalJobs": 1,
           "dubbels": [],
           "eerstePublicatieDatum": "2025-08-29T16:10:18Z",
           "gesloten": false,
           "id": {
              "id": 71826912
           },
           "laatsteWijzigingDatum": "2025-08-29T16:10:18Z",
           "leverancier": {
              "gemandateerd": true,
              "type": "GEWONE_BEDRIJVEN"
           },
           "locatie": {},
           "tewerkstellingsLocatieRegioOfAdres": "GENT",
           "vacatureBedrijfsnaam": "Rekruut",
           "vacaturefunctie": {
              "arbeidscircuitLijn": "Vaste Job",
              "naam": "Full Cycle Sales"
           }
        }
     ],
     "totaalAantal": 754
  }
```