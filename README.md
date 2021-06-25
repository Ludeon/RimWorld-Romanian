A Romanian translation for RimWorld.

See this page for license info:

http://ludeon.com/forums/index.php?topic=2933.0

Current status
--------------------------------------
The last "structural update" (step 18. from Tynan's guide): 1.2.3005

There's still a lot to be translated. Check the issues tab.

General Notes
--------------------------------------
- Each XML entry has a comment above containing the English translation. You might want to have the [French translation](https://github.com/Ludeon/RimWorld-fr) opened in a separate tab when translating, for reference.
- XML entries containing the `TODO` string are ignored by the game (the English default will be shown instead).
- XML entries having the comment `<!-- UNUSED -->` above are outdated translations from a previous version of the game, kept as a reference. They should be integrated in the newer tags, or outright deleted altogether.
- Romanian has gendered nouns. Some tags admit a female version (e.g. `<title>` and `<titleFemale>` in `Backstories.xml`). Cross-check the [French translation](https://github.com/Ludeon/RimWorld-fr) for inspiration.

Progress overview
--------------------------------------
The following table is generated from a python script.

|EN_words|%done|Path|
|-:|-:|:-|
| 31562|  0.00|Core\Backstories\Backstories.xml                                           |
| 31562|  0.00|Core\Backstories                                                           |
|     5|  0.00|Core\DefInjected\ApparelLayerDef                                           |
|    10|  0.00|Core\DefInjected\BillRepeatModeDef                                         |
|    10|  0.00|Core\DefInjected\BillStoreModeDef                                          |
|   144| 58.33|Core\DefInjected\BiomeDef\Biomes_Cold.xml                                  |
|   102|100.00|Core\DefInjected\BiomeDef\Biomes_WarmArid.xml                              |
|   409| 64.30|Core\DefInjected\BiomeDef                                                  |
|   570|  3.16|Core\DefInjected\BodyDef\Bodies_Animal_Quadruped.xml                       |
|   113|  0.88|Core\DefInjected\BodyDef\Bodies_Humanlike.xml                              |
|   162|  1.85|Core\DefInjected\BodyDef\Bodies_Mechanoid.xml                              |
|   943|  2.97|Core\DefInjected\BodyDef                                                   |
|   237| 75.11|Core\DefInjected\BodyPartDef                                               |
|    61| 73.77|Core\DefInjected\BodyPartGroupDef                                          |
|     7| 85.71|Core\DefInjected\ChemicalDef                                               |
|   621|  0.00|Core\DefInjected\ConceptDef\Concepts_NotedOpportunistic.xml                |
|  1280|  0.00|Core\DefInjected\ConceptDef\Concepts_NotedSelfshow.xml                     |
|   197| 46.70|Core\DefInjected\ConceptDef\Concepts_TriggeredModal.xml                    |
|  2121|  5.23|Core\DefInjected\ConceptDef                                                |
|   197| 11.17|Core\DefInjected\DamageDef                                                 |
|    12|  0.00|Core\DefInjected\DesignationCategoryDef                                    |
|    11|  0.00|Core\DefInjected\DesignatorDropdownGroupDef                                |
|   298| 32.21|Core\DefInjected\DifficultyDef\Difficulties.xml                            |
|   298| 32.21|Core\DefInjected\DifficultyDef                                             |
|     1|  0.00|Core\DefInjected\DutyDef                                                   |
|   214|  0.00|Core\DefInjected\ExpansionDef\ExpansionDefs.xml                            |
|   214|  0.00|Core\DefInjected\ExpansionDef                                              |
|    11|  0.00|Core\DefInjected\ExpectationDef                                            |
|   484|  0.00|Core\DefInjected\FactionDef\Factions_Misc.xml                              |
|   526|  2.47|Core\DefInjected\FactionDef                                                |
|   718|  0.00|Core\DefInjected\GameConditionDef\GameConditions_Misc.xml                  |
|   741|  0.00|Core\DefInjected\GameConditionDef                                          |
|    34|  0.00|Core\DefInjected\GatheringDef                                              |
|    58|  0.00|Core\DefInjected\HairDef                                                   |
|   113|  0.00|Core\DefInjected\HediffDef\Alcohol_Beer.xml                                |
|   103|  0.00|Core\DefInjected\HediffDef\GoJuice.xml                                     |
|   447|  0.00|Core\DefInjected\HediffDef\Hediffs_Global_Misc.xml                         |
|   145|  0.00|Core\DefInjected\HediffDef\Hediffs_Global_Temperature.xml                  |
|   224|  0.00|Core\DefInjected\HediffDef\Hediffs_Local_Chronic.xml                       |
|   255|  0.00|Core\DefInjected\HediffDef\Hediffs_Local_Infections.xml                    |
|   264|  0.00|Core\DefInjected\HediffDef\Hediffs_Local_Injuries.xml                      |
|   211|  0.00|Core\DefInjected\HediffDef\Hediffs_Local_Misc.xml                          |
|   109|  0.00|Core\DefInjected\HediffDef\Psychite_Yayo.xml                               |
|   101|  0.00|Core\DefInjected\HediffDef\Smokeleaf.xml                                   |
|   116|  0.00|Core\DefInjected\HediffDef\WakeUp.xml                                      |
|  2657|  0.00|Core\DefInjected\HediffDef                                                 |
|    13|  0.00|Core\DefInjected\HediffGiverSetDef                                         |
|    29|  0.00|Core\DefInjected\HistoryAutoRecorderDef                                    |
|     5|  0.00|Core\DefInjected\HistoryAutoRecorderGroupDef                               |
|   400|  0.00|Core\DefInjected\IncidentDef\Incidents_Map_Disease.xml                     |
|   194|  0.00|Core\DefInjected\IncidentDef\Incidents_Map_Misc.xml                        |
|   265|  0.00|Core\DefInjected\IncidentDef\Incidents_Map_Threats.xml                     |
|   940|  0.00|Core\DefInjected\IncidentDef                                               |
|   269|  0.00|Core\DefInjected\InspirationDef\Inspirations.xml                           |
|   269|  0.00|Core\DefInjected\InspirationDef                                            |
|  1635|  0.00|Core\DefInjected\InstructionDef\Instructions.xml                           |
|  1635|  0.00|Core\DefInjected\InstructionDef                                            |
|   296|  0.00|Core\DefInjected\InteractionDef\Interactions_Animal.xml                    |
|   199|  0.00|Core\DefInjected\InteractionDef\Interactions_Prisoner.xml                  |
|   189|  0.00|Core\DefInjected\InteractionDef\Interactions_Romance.xml                   |
|   215|  0.00|Core\DefInjected\InteractionDef\Interactions_Social.xml                    |
|   899|  0.00|Core\DefInjected\InteractionDef                                            |
|   136|  0.00|Core\DefInjected\JobDef\Jobs_Misc.xml                                      |
|   117|  0.00|Core\DefInjected\JobDef\Jobs_Work.xml                                      |
|   316|  0.00|Core\DefInjected\JobDef                                                    |
|    16|  0.00|Core\DefInjected\JoyKindDef                                                |
|    73|  0.00|Core\DefInjected\KeyBindingCategoryDef                                     |
|   119|  0.00|Core\DefInjected\KeyBindingDef\KeyBindings.xml                             |
|   119|  0.00|Core\DefInjected\KeyBindingDef                                             |
|    14|  0.00|Core\DefInjected\LifeStageDef                                              |
|   130|  0.00|Core\DefInjected\MainButtonDef\MainButtons.xml                             |
|   130|  0.00|Core\DefInjected\MainButtonDef                                             |
|     6|  0.00|Core\DefInjected\MeditationFocusDef                                        |
|     3|  0.00|Core\DefInjected\MentalBreakDef                                            |
|   519|  0.00|Core\DefInjected\MentalStateDef\MentalStates_Mood.xml                      |
|   599|  0.00|Core\DefInjected\MentalStateDef                                            |
|   286|  0.00|Core\DefInjected\NeedDef\Needs.xml                                         |
|   426|  0.00|Core\DefInjected\NeedDef                                                   |
|    20|  0.00|Core\DefInjected\PawnCapacityDef                                           |
|    51|  0.00|Core\DefInjected\PawnColumnDef                                             |
|   302|  0.00|Core\DefInjected\PawnKindDef                                               |
|    52|  0.00|Core\DefInjected\PawnRelationDef                                           |
|   258|  0.00|Core\DefInjected\PawnsArrivalModeDef\PawnsArrivalModes.xml                 |
|   258|  0.00|Core\DefInjected\PawnsArrivalModeDef                                       |
|     7|  0.00|Core\DefInjected\PrisonerInteractionModeDef                                |
|   264|  0.00|Core\DefInjected\QuestScriptDef\Scripts_Utility_ThreatsCore.xml            |
|   138|  0.00|Core\DefInjected\QuestScriptDef\Script_BanditCamp.xml                      |
|   111|  0.00|Core\DefInjected\QuestScriptDef\Script_DownedRefugee.xml                   |
|  1161|  0.00|Core\DefInjected\QuestScriptDef                                            |
|   235|  0.00|Core\DefInjected\RaidStrategyDef\RaidStrategies.xml                        |
|   235|  0.00|Core\DefInjected\RaidStrategyDef                                           |
|   182|  0.00|Core\DefInjected\RecipeDef\Recipes_Meals.xml                               |
|   191|  0.00|Core\DefInjected\RecipeDef\Recipes_Production.xml                          |
|   926|  0.00|Core\DefInjected\RecipeDef                                                 |
|   414|  0.00|Core\DefInjected\RecordDef\Records_Misc.xml                                |
|   219|  0.00|Core\DefInjected\RecordDef\Records_Time.xml                                |
|   633|  0.00|Core\DefInjected\RecordDef                                                 |
|   328|  0.00|Core\DefInjected\ResearchProjectDef\ResearchProjects_1.xml                 |
|   337|  0.00|Core\DefInjected\ResearchProjectDef\ResearchProjects_2_Electricity.xml     |
|   213|  0.00|Core\DefInjected\ResearchProjectDef\ResearchProjects_3_Microelectronics.xml|
|   245|  0.00|Core\DefInjected\ResearchProjectDef\ResearchProjects_4_MultiAnalyzer.xml   |
|   289|  0.00|Core\DefInjected\ResearchProjectDef\ResearchProjects_5_Ship.xml            |
|  1412|  0.00|Core\DefInjected\ResearchProjectDef                                        |
|     1|  0.00|Core\DefInjected\ResearchTabDef                                            |
|     6|  0.00|Core\DefInjected\RiverDef                                                  |
|    12|  0.00|Core\DefInjected\RoadDef                                                   |
|     7|  0.00|Core\DefInjected\RoofDef                                                   |
|    18|  0.00|Core\DefInjected\RoomRoleDef                                               |
|    65|  0.00|Core\DefInjected\RoomStatDef                                               |
|   543|  0.00|Core\DefInjected\RulePackDef\RulePacks_Art_Descriptions.xml                |
|   145|  0.00|Core\DefInjected\RulePackDef\RulePacks_Art_DescriptionsPhysical.xml        |
|   141|  0.00|Core\DefInjected\RulePackDef\RulePacks_Art_ImagesTaleless.xml              |
|   243|  0.00|Core\DefInjected\RulePackDef\RulePacks_CombatIncludes.xml                  |
|   300|  0.00|Core\DefInjected\RulePackDef\RulePacks_CombatMelee.xml                     |
|   652|  0.00|Core\DefInjected\RulePackDef\RulePacks_CombatRanged.xml                    |
|   136|  0.00|Core\DefInjected\RulePackDef\RulePacks_DamageEvent.xml                     |
|   137|  0.00|Core\DefInjected\RulePackDef\RulePacks_Global.xml                          |
|   388|  0.00|Core\DefInjected\RulePackDef\RulePacks_Maneuvers.xml                       |
|   109|  0.00|Core\DefInjected\RulePackDef\RulePacks_Namers_Art.xml                      |
|   264|  0.00|Core\DefInjected\RulePackDef\RulePacks_Namers_Factions.xml                 |
|   258|  0.00|Core\DefInjected\RulePackDef\RulePacks_Namers_WorldFeatures.xml            |
|   176|  0.00|Core\DefInjected\RulePackDef\RulePacks_Transitions.xml                     |
|  3919|  0.00|Core\DefInjected\RulePackDef                                               |
|   683|  0.00|Core\DefInjected\ScenarioDef\Scenarios_Classic.xml                         |
|   683|  0.00|Core\DefInjected\ScenarioDef                                               |
|    72|  0.00|Core\DefInjected\ScenPartDef                                               |
|   148|  0.00|Core\DefInjected\SitePartDef                                               |
|   120| 18.33|Core\DefInjected\SkillDef\Skills.xml                                       |
|   120| 18.33|Core\DefInjected\SkillDef                                                  |
|   136|  0.00|Core\DefInjected\SpecialThingFilterDef\SpecialThingFilters.xml             |
|   136|  0.00|Core\DefInjected\SpecialThingFilterDef                                     |
|    40|  0.00|Core\DefInjected\StatCategoryDef                                           |
|   159|  0.00|Core\DefInjected\StatDef\Stats_Abilities.xml                               |
|   571|  0.00|Core\DefInjected\StatDef\Stats_Apparel.xml                                 |
|   273|  0.00|Core\DefInjected\StatDef\Stats_Basics_General.xml                          |
|   180|  0.00|Core\DefInjected\StatDef\Stats_Basics_Special.xml                          |
|   195|  0.00|Core\DefInjected\StatDef\Stats_Building_Special.xml                        |
|   152|  0.00|Core\DefInjected\StatDef\Stats_Pawns_Combat.xml                            |
|   300|  0.00|Core\DefInjected\StatDef\Stats_Pawns_General.xml                           |
|   179|  0.00|Core\DefInjected\StatDef\Stats_Pawns_Social.xml                            |
|   280|  0.00|Core\DefInjected\StatDef\Stats_Pawns_WorkGeneral.xml                       |
|   111|  0.00|Core\DefInjected\StatDef\Stats_Pawns_WorkMedical.xml                       |
|   237|  0.00|Core\DefInjected\StatDef\Stats_Pawns_WorkRecipes.xml                       |
|   100|  0.00|Core\DefInjected\StatDef\Stats_Stuff.xml                                   |
|   142|  0.00|Core\DefInjected\StatDef\Stats_Weapons_Melee.xml                           |
|   122|  0.00|Core\DefInjected\StatDef\Stats_Weapons_Ranged.xml                          |
|  3001|  0.00|Core\DefInjected\StatDef                                                   |
|   118| 98.31|Core\DefInjected\StorytellerDef\Storytellers.xml                           |
|   118| 98.31|Core\DefInjected\StorytellerDef                                            |
|     5|  0.00|Core\DefInjected\StuffCategoryDef                                          |
|   546|  0.00|Core\DefInjected\TaleDef\Tales_Caravan.xml                                 |
|  1188|  0.00|Core\DefInjected\TaleDef\Tales_DoublePawn.xml                              |
|   338|  0.00|Core\DefInjected\TaleDef\Tales_DoublePawn_Relationships.xml                |
|   340|  0.00|Core\DefInjected\TaleDef\Tales_Event.xml                                   |
|  1526|  0.00|Core\DefInjected\TaleDef\Tales_Health.xml                                  |
|  1887|  0.00|Core\DefInjected\TaleDef\Tales_Incident.xml                                |
|  1638|  0.00|Core\DefInjected\TaleDef\Tales_Job.xml                                     |
|  1407|  0.00|Core\DefInjected\TaleDef\Tales_SinglePawn.xml                              |
|  8870|  0.00|Core\DefInjected\TaleDef                                                   |
|    11|  0.00|Core\DefInjected\TerrainAffordanceDef                                      |
|   184|  0.00|Core\DefInjected\TerrainDef\Terrain_Floors.xml                             |
|   245|  0.00|Core\DefInjected\TerrainDef\Terrain_Floors_StoneTile.xml                   |
|   531|  0.00|Core\DefInjected\TerrainDef                                                |
|    80|  0.00|Core\DefInjected\ThingCategoryDef                                          |
|   225|  0.00|Core\DefInjected\ThingDef\Apparel_Headgear.xml                             |
|   290|  0.00|Core\DefInjected\ThingDef\Apparel_Various.xml                              |
|   132|  0.00|Core\DefInjected\ThingDef\Buildings_Exotic.xml                             |
|   575|  0.00|Core\DefInjected\ThingDef\Buildings_Furniture.xml                          |
|   256|  0.00|Core\DefInjected\ThingDef\Buildings_Joy.xml                                |
|   516|  0.00|Core\DefInjected\ThingDef\Buildings_Misc.xml                               |
|   150|  0.00|Core\DefInjected\ThingDef\Buildings_Natural.xml                            |
|   163|  0.00|Core\DefInjected\ThingDef\Buildings_Power.xml                              |
|   458|  0.00|Core\DefInjected\ThingDef\Buildings_Production.xml                         |
|   346|  0.00|Core\DefInjected\ThingDef\Buildings_Security.xml                           |
|   236|  0.00|Core\DefInjected\ThingDef\Buildings_Security_Turrets.xml                   |
|   139|  0.00|Core\DefInjected\ThingDef\Buildings_Ship.xml                               |
|   131|  0.00|Core\DefInjected\ThingDef\Buildings_Temperature.xml                        |
|   210|  0.00|Core\DefInjected\ThingDef\Hediffs_BodyParts_Archotech.xml                  |
|   306|  0.00|Core\DefInjected\ThingDef\Hediffs_BodyParts_Bionic.xml                     |
|   290|  0.00|Core\DefInjected\ThingDef\Hediffs_BodyParts_Prosthetic.xml                 |
|   257|  0.00|Core\DefInjected\ThingDef\Items_Exotic.xml                                 |
|   136|  0.00|Core\DefInjected\ThingDef\Items_Food.xml                                   |
|   377|  0.00|Core\DefInjected\ThingDef\Items_Resource_AnimalProduct.xml                 |
|   161|  0.00|Core\DefInjected\ThingDef\Items_Resource_Manufactured.xml                  |
|   199|  0.00|Core\DefInjected\ThingDef\Items_Resource_Shell.xml                         |
|   361|  0.00|Core\DefInjected\ThingDef\Items_Resource_Stuff.xml                         |
|   403|  0.00|Core\DefInjected\ThingDef\Items_Resource_Stuff_Leather.xml                 |
|   125|  0.00|Core\DefInjected\ThingDef\MeleeNeolithic.xml                               |
|   406|  0.00|Core\DefInjected\ThingDef\Plants_Cultivated_Farm.xml                       |
|   116|  0.00|Core\DefInjected\ThingDef\Plants_Wild_Swamp.xml                            |
|   165|  0.00|Core\DefInjected\ThingDef\Plants_Wild_Temperate.xml                        |
|   178|  0.00|Core\DefInjected\ThingDef\Plants_Wild_Tropical.xml                         |
|   209|  0.00|Core\DefInjected\ThingDef\Races_Animal_Arid.xml                            |
|   120|  0.00|Core\DefInjected\ThingDef\Races_Animal_Bears.xml                           |
|   142|  0.00|Core\DefInjected\ThingDef\Races_Animal_BigCats.xml                         |
|   125|  0.00|Core\DefInjected\ThingDef\Races_Animal_Birds.xml                           |
|   441|  0.00|Core\DefInjected\ThingDef\Races_Animal_Farm.xml                            |
|   265|  0.00|Core\DefInjected\ThingDef\Races_Animal_Giant.xml                           |
|   151|  0.00|Core\DefInjected\ThingDef\Races_Animal_Insect.xml                          |
|   140|  0.00|Core\DefInjected\ThingDef\Races_Animal_Pet.xml                             |
|   220|  0.00|Core\DefInjected\ThingDef\Races_Animal_Rodentlike.xml                      |
|   208|  0.00|Core\DefInjected\ThingDef\Races_Animal_Temperate.xml                       |
|   127|  0.00|Core\DefInjected\ThingDef\Races_Animal_Tropical.xml                        |
|   224|  0.00|Core\DefInjected\ThingDef\Races_Animal_WildCanines.xml                     |
|   157|  0.00|Core\DefInjected\ThingDef\Races_Mechanoid.xml                              |
|   438|  0.00|Core\DefInjected\ThingDef\RangedIndustrial.xml                             |
|   103|  0.00|Core\DefInjected\ThingDef\RangedNeolithic.xml                              |
|   227|  0.00|Core\DefInjected\ThingDef\RangedSpecial.xml                                |
|   305|  0.00|Core\DefInjected\ThingDef\Various_Stone.xml                                |
| 13154|  0.00|Core\DefInjected\ThingDef                                                  |
|   438|  0.00|Core\DefInjected\ThoughtDef\Thoughts_Memory_Death.xml                      |
|   260|  0.00|Core\DefInjected\ThoughtDef\Thoughts_Memory_Eating.xml                     |
|   122|  0.00|Core\DefInjected\ThoughtDef\Thoughts_Memory_Gatherings.xml                 |
|   380|  0.00|Core\DefInjected\ThoughtDef\Thoughts_Memory_Lost.xml                       |
|   554|  0.00|Core\DefInjected\ThoughtDef\Thoughts_Memory_Misc.xml                       |
|   512|  0.00|Core\DefInjected\ThoughtDef\Thoughts_Memory_RoomStats.xml                  |
|   334|  0.00|Core\DefInjected\ThoughtDef\Thoughts_Memory_Social.xml                     |
|   378|  0.00|Core\DefInjected\ThoughtDef\Thoughts_Situation_General.xml                 |
|   631|  0.00|Core\DefInjected\ThoughtDef\Thoughts_Situation_Needs.xml                   |
|   344|  0.00|Core\DefInjected\ThoughtDef\Thoughts_Situation_RoomStats.xml               |
|   154|  0.00|Core\DefInjected\ThoughtDef\Thoughts_Situation_Social.xml                  |
|   262|  0.00|Core\DefInjected\ThoughtDef\Thoughts_Situation_Special.xml                 |
|   621|  0.00|Core\DefInjected\ThoughtDef\Thoughts_Situation_Traits.xml                  |
|  5391|  0.00|Core\DefInjected\ThoughtDef                                                |
|     4|  0.00|Core\DefInjected\TimeAssignmentDef                                         |
|  1042|  0.00|Core\DefInjected\TipSetDef\Tips.xml                                        |
|  1042|  0.00|Core\DefInjected\TipSetDef                                                 |
|    14|  0.00|Core\DefInjected\ToolCapacityDef                                           |
|    29|  0.00|Core\DefInjected\TraderKindDef                                             |
|     4|  0.00|Core\DefInjected\TrainabilityDef                                           |
|    75|  0.00|Core\DefInjected\TrainableDef                                              |
|   769|  0.00|Core\DefInjected\TraitDef\Traits_Singular.xml                              |
|   657|  0.00|Core\DefInjected\TraitDef\Traits_Spectrum.xml                              |
|  1426|  0.00|Core\DefInjected\TraitDef                                                  |
|    10|  0.00|Core\DefInjected\TransferableSorterDef                                     |
|   111|  0.00|Core\DefInjected\WeatherDef\Weathers.xml                                   |
|   111|  0.00|Core\DefInjected\WeatherDef                                                |
|   511|  0.00|Core\DefInjected\WorkGiverDef\WorkGivers.xml                               |
|   511|  0.00|Core\DefInjected\WorkGiverDef                                              |
|   287| 83.62|Core\DefInjected\WorkTypeDef\WorkTypes.xml                                 |
|   287| 83.62|Core\DefInjected\WorkTypeDef                                               |
|    68|  0.00|Core\DefInjected\WorldObjectDef                                            |
| 59081|  1.93|Core\DefInjected                                                           |
|  1411| 43.16|Core\Keyed\Alerts.xml                                                      |
|   690| 45.07|Core\Keyed\Designators.xml                                                 |
|  3490| 12.89|Core\Keyed\Dialogs_Various.xml                                             |
|  1598|  1.63|Core\Keyed\Dialog_StatsReports.xml                                         |
|   231| 46.75|Core\Keyed\Dialog_Trees.xml                                                |
|   207| 18.84|Core\Keyed\Enums.xml                                                       |
|   679| 27.39|Core\Keyed\FloatMenu.xml                                                   |
|  1405| 24.91|Core\Keyed\GameplayCommands.xml                                            |
|  1172| 25.51|Core\Keyed\Incidents.xml                                                   |
|   483| 20.50|Core\Keyed\ITabs.xml                                                       |
|  2291|  7.73|Core\Keyed\Letters.xml                                                     |
|   855|  7.25|Core\Keyed\MainTabs.xml                                                    |
|  2127| 14.20|Core\Keyed\Menus_Main.xml                                                  |
|   209| 33.49|Core\Keyed\Menu_Options.xml                                                |
|  1940| 10.05|Core\Keyed\Messages.xml                                                    |
|   357| 35.29|Core\Keyed\Misc.xml                                                        |
|  2579| 16.67|Core\Keyed\Misc_Gameplay.xml                                               |
|   127|  0.00|Core\Keyed\ScenParts.xml                                                   |
|   102|  0.00|Core\Keyed\WITabs.xml                                                      |
| 22406| 18.27|Core\Keyed                                                                 |
|113049|  4.63|Core                                                                       |
|   919|  0.00|Royalty\DefInjected\AbilityDef\Abilities.xml                               |
|   919|  0.00|Royalty\DefInjected\AbilityDef                                             |
|    74|  0.00|Royalty\DefInjected\ConceptDef                                             |
|     1|  0.00|Royalty\DefInjected\DutyDef                                                |
|    92|  0.00|Royalty\DefInjected\FactionDef                                             |
|   251|  0.00|Royalty\DefInjected\GameConditionDef\Buildings_ConditionCausers.xml        |
|   251|  0.00|Royalty\DefInjected\GameConditionDef                                       |
|    82|  0.00|Royalty\DefInjected\GatheringDef                                           |
|    11|  0.00|Royalty\DefInjected\HairDef                                                |
|   143|  0.00|Royalty\DefInjected\HediffDef\Hediffs_BodyParts_Bionic_Empire.xml          |
|   138|  0.00|Royalty\DefInjected\HediffDef\Hediffs_Local_Misc.xml                       |
|   379|  0.00|Royalty\DefInjected\HediffDef\Hediffs_Psycasts.xml                         |
|   842|  0.00|Royalty\DefInjected\HediffDef                                              |
|   225|  0.00|Royalty\DefInjected\IncidentDef                                            |
|    70|  0.00|Royalty\DefInjected\InteractionDef                                         |
|    11|  0.00|Royalty\DefInjected\JobDef                                                 |
|     1|  0.00|Royalty\DefInjected\JoyKindDef                                             |
|     6|  0.00|Royalty\DefInjected\MentalStateDef                                         |
|     2|  0.00|Royalty\DefInjected\NeedDef                                                |
|    30|  0.00|Royalty\DefInjected\PawnKindDef                                            |
|   155|  0.00|Royalty\DefInjected\QuestScriptDef\Scripts_Decree.xml                      |
|   682|  0.00|Royalty\DefInjected\QuestScriptDef\Scripts_ItemPodThreat.xml               |
|   932|  0.00|Royalty\DefInjected\QuestScriptDef\Scripts_JoinerThreat.xml                |
|   100|  0.00|Royalty\DefInjected\QuestScriptDef\Scripts_Missions.xml                    |
|   104|  0.00|Royalty\DefInjected\QuestScriptDef\Scripts_Permits.xml                     |
|   101|  0.00|Royalty\DefInjected\QuestScriptDef\Scripts_RewardMechpods.xml              |
|   140|  0.00|Royalty\DefInjected\QuestScriptDef\Scripts_RewardRaid.xml                  |
|   104|  0.00|Royalty\DefInjected\QuestScriptDef\Scripts_Utility_Helpers.xml             |
|   119|  0.00|Royalty\DefInjected\QuestScriptDef\Script_BuildMonument_Worker.xml         |
|   201|  0.00|Royalty\DefInjected\QuestScriptDef\Script_ChangeRoyalHeir.xml              |
|   484|  0.00|Royalty\DefInjected\QuestScriptDef\Script_EndGame_RoyalAscent.xml          |
|   705|  0.00|Royalty\DefInjected\QuestScriptDef\Script_Hospitality_Refugee.xml          |
|   426|  0.00|Royalty\DefInjected\QuestScriptDef\Script_Hospitality_Root_Animals.xml     |
|   724|  0.00|Royalty\DefInjected\QuestScriptDef\Script_Hospitality_Root_Joiners.xml     |
|   467|  0.00|Royalty\DefInjected\QuestScriptDef\Script_Hospitality_Root_Prisoners.xml   |
|   274|  0.00|Royalty\DefInjected\QuestScriptDef\Script_Hospitality_Worker.xml           |
|   146|  0.00|Royalty\DefInjected\QuestScriptDef\Script_Intro_Deserter.xml               |
|   260|  0.00|Royalty\DefInjected\QuestScriptDef\Script_Intro_Wimp.xml                   |
|   162|  0.00|Royalty\DefInjected\QuestScriptDef\Script_PawnLend.xml                     |
|   315|  0.00|Royalty\DefInjected\QuestScriptDef\Script_ShuttleCrash_Rescue.xml          |
|  7027|  0.00|Royalty\DefInjected\QuestScriptDef                                         |
|   272|  0.00|Royalty\DefInjected\RecipeDef\Hediffs_BodyParts_Bionic_Empire.xml          |
|   121|  0.00|Royalty\DefInjected\RecipeDef\Hediffs_BodyParts_Prosthetic_Empire.xml      |
|   531|  0.00|Royalty\DefInjected\RecipeDef                                              |
|   173|  0.00|Royalty\DefInjected\ResearchProjectDef\ResearchProjects_Implants.xml       |
|   277|  0.00|Royalty\DefInjected\ResearchProjectDef                                     |
|     2|  0.00|Royalty\DefInjected\RoomRoleDef                                            |
|   697|  0.00|Royalty\DefInjected\RoyalTitleDef\RoyalTitles_Empire.xml                   |
|   697|  0.00|Royalty\DefInjected\RoyalTitleDef                                          |
|   226|  0.00|Royalty\DefInjected\RoyalTitlePermitDef\RoyalPermits_Empire.xml            |
|   226|  0.00|Royalty\DefInjected\RoyalTitlePermitDef                                    |
|   181|  0.00|Royalty\DefInjected\RulePackDef\Script_BuildMonument_TextCommon.xml        |
|   267|  0.00|Royalty\DefInjected\RulePackDef\Script_Hospitality_TextCommon.xml          |
|   623|  0.00|Royalty\DefInjected\RulePackDef                                            |
|   137|  0.00|Royalty\DefInjected\SitePartDef                                            |
|    72|  0.00|Royalty\DefInjected\StatDef                                                |
|    86|  0.00|Royalty\DefInjected\TaleDef                                                |
|   120|  0.00|Royalty\DefInjected\TerrainDef                                             |
|   115|  0.00|Royalty\DefInjected\ThingDef\Apparel_Packs.xml                             |
|   113|  0.00|Royalty\DefInjected\ThingDef\Apparel_Psychic.xml                           |
|   119|  0.00|Royalty\DefInjected\ThingDef\Apparel_Royal.xml                             |
|   731|  0.00|Royalty\DefInjected\ThingDef\Apparel_Various.xml                           |
|   261|  0.00|Royalty\DefInjected\ThingDef\Buildings_ConditionCausers.xml                |
|   117|  0.00|Royalty\DefInjected\ThingDef\Buildings_Furniture.xml                       |
|   138|  0.00|Royalty\DefInjected\ThingDef\Buildings_Mech.xml                            |
|   106|  0.00|Royalty\DefInjected\ThingDef\Buildings_Mech_ShieldGenerators.xml           |
|   113|  0.00|Royalty\DefInjected\ThingDef\Buildings_Mech_Turrets.xml                    |
|   264|  0.00|Royalty\DefInjected\ThingDef\Buildings_Misc.xml                            |
|   165|  0.00|Royalty\DefInjected\ThingDef\Buildings_MusicalInstruments.xml              |
|   668|  0.00|Royalty\DefInjected\ThingDef\Hediffs_BodyParts_Bionic_Empire.xml           |
|   325|  0.00|Royalty\DefInjected\ThingDef\Hediffs_BodyParts_Prosthetic_Empire.xml       |
|   244|  0.00|Royalty\DefInjected\ThingDef\MeleeBladelink.xml                            |
|   326|  0.00|Royalty\DefInjected\ThingDef\Plants_Wild.xml                               |
|  4496|  0.00|Royalty\DefInjected\ThingDef                                               |
|   110|  0.00|Royalty\DefInjected\ThoughtDef\Thoughts_Memory_RoomStats.xml               |
|   135|  0.00|Royalty\DefInjected\ThoughtDef\WeaponTraitDefs.xml                         |
|   601|  0.00|Royalty\DefInjected\ThoughtDef                                             |
|     1|  0.00|Royalty\DefInjected\TimeAssignmentDef                                      |
|   302|  0.00|Royalty\DefInjected\TipSetDef\Tips.xml                                     |
|   302|  0.00|Royalty\DefInjected\TipSetDef                                              |
|     7|  0.00|Royalty\DefInjected\TraderKindDef                                          |
|   443|  0.00|Royalty\DefInjected\WeaponTraitDef\WeaponTraitDefs.xml                     |
|   443|  0.00|Royalty\DefInjected\WeaponTraitDef                                         |
|     5|  0.00|Royalty\DefInjected\WorldObjectDef                                         |
| 18270|  0.00|Royalty\DefInjected                                                        |
|   381|  0.00|Royalty\Keyed\Alerts.xml                                                   |
|   318|  0.00|Royalty\Keyed\Dialogs_Various.xml                                          |
|   130|  0.00|Royalty\Keyed\Dialog_StatReports.xml                                       |
|   308|  0.00|Royalty\Keyed\GameplayCommands.xml                                         |
|   223|  0.00|Royalty\Keyed\ITabs.xml                                                    |
|   877|  0.00|Royalty\Keyed\Letters.xml                                                  |
|   103|  0.00|Royalty\Keyed\Messages.xml                                                 |
|   517|  0.00|Royalty\Keyed\Misc_Gameplay.xml                                            |
|  2985|  0.00|Royalty\Keyed                                                              |
| 21255|  0.00|Royalty                                                                    |
|134304|  3.90|.                                                                          |