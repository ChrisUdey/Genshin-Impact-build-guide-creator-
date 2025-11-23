from app.database import SessionLocal, Base, engine
from app.models.artifact import Artifact
from app.models.domain_artifact import DomainArtifact

def seed_artifacts():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # Send help
    try:
        artifacts = [
            Artifact(artifactID="adventurer", name="Adventurer", max_rarity=3,
                     two_set_bonus="Max HP increased by 1000.",
                     four_set_bonus="Opening a chest regenerates 30% Max HP over 5s.",
                     image=""
                     ),
            Artifact(artifactID="archaic-petra", name="Archaic Petra", max_rarity=5,
                     two_set_bonus="Geo DMG Bonus +15%",
                     four_set_bonus="Upon obtaining an Elemental Shard created through a Crystallize Reaction, all party members gain 35% DMG Bonus for that particular element for 10s...",
                     image=""
                     ),
            Artifact(artifactID="berserker", name="Berserker", max_rarity=4,
                     two_set_bonus="CRIT Rate +12%",
                     four_set_bonus="When HP is below 70%, CRIT Rate increases by an additional 24%.",
                     image=""
                     ),
            Artifact(artifactID="blizzard-strayer", name="Blizzard Strayer", max_rarity=5,
                     two_set_bonus="Cryo DMG Bonus +15%",
                     four_set_bonus="When a character attacks an opponent affected by Cryo...",
                     image=""
                     ),
            Artifact(artifactID="bloodstained-chivalry", name="Bloodstained Chivalry", max_rarity=5,
                     two_set_bonus="Physical DMG Bonus +25%",
                     four_set_bonus="After defeating an opponent, increases Charged Attack DMG by 50%...",
                     image=""
                     ),
            Artifact(artifactID="brave-heart", name="Brave Heart", max_rarity=4,
                     two_set_bonus="ATK +18%",
                     four_set_bonus="Increases DMG by 30% against opponents with more than 50% HP.",
                     image=""
                     ),
            Artifact(artifactID="crimson-witch-of-flames", name="Crimson Witch of Flames", max_rarity=5,
                     two_set_bonus="Pyro DMG Bonus +15%",
                     four_set_bonus="Increases Overloaded and Burning DMG by 40%...",
                     image=""
                     ),
            Artifact(artifactID="deepwood-memories", name="Deepwood Memories", max_rarity=5,
                     two_set_bonus="Dendro DMG Bonus +15%",
                     four_set_bonus="After Elemental Skills or Bursts hit opponents...",
                     image=""
                     ),
            Artifact(artifactID="defenders-will", name="Defender's Will", max_rarity=4,
                     two_set_bonus="DEF +30%",
                     four_set_bonus="For each different element present in your party...",
                     image=""
                     ),
            Artifact(artifactID="desert-pavilion-chronicle", name="Desert Pavilion Chronicle", max_rarity=5,
                     two_set_bonus="Anemo DMG Bonus +15%",
                     four_set_bonus="When Charged Attacks hit opponents...",
                     image=""
                     ),
            Artifact(artifactID="echoes-of-an-offering", name="Echoes of an Offering", max_rarity=5,
                     two_set_bonus="ATK +18%",
                     four_set_bonus="When Normal Attacks hit opponents...",
                     image=""
                     ),
            Artifact(artifactID="emblem-of-severed-fate", name="Emblem of Severed Fate", max_rarity=5,
                     two_set_bonus="Energy Recharge +20%",
                     four_set_bonus="Increases Elemental Burst DMG by 25% of Energy Recharge...",
                     image=""
                     ),
            Artifact(artifactID="flower-of-paradise-lost", name="Flower of Paradise Lost", max_rarity=5,
                     two_set_bonus="Elemental Mastery +80",
                     four_set_bonus="The equipping character's Bloom, Hyperbloom...",
                     image=""
                     ),
            Artifact(artifactID="fragment-of-harmonic-whimsy", name="Fragment of Harmonic Whimsy", max_rarity=5,
                     two_set_bonus="ATK +18%",
                     four_set_bonus="When the value of a Bond of Life increases...",
                     image=""
                     ),
            Artifact(artifactID="gambler", name="Gambler", max_rarity=4,
                     two_set_bonus="Increases Elemental Skill DMG by 20%.",
                     four_set_bonus="Defeating an opponent has 100% chance to remove Elemental Skill CD...",
                     image=""
                     ),
            Artifact(artifactID="gilded-dreams", name="Gilded Dreams", max_rarity=5,
                     two_set_bonus="Elemental Mastery +80",
                     four_set_bonus="Within 8s of triggering an Elemental Reaction...",
                     image=""
                     ),
            Artifact(artifactID="glacier-and-snowfield", name="Glacier and Snowfield", max_rarity=5,
                     two_set_bonus="Cryo DMG Bonus +15%",
                     four_set_bonus="When other nearby party members use Elemental Skills...",
                     image=""
                     ),
            Artifact(artifactID="gladiators-finale", name="Gladiator's Finale", max_rarity=5,
                     two_set_bonus="ATK +18%",
                     four_set_bonus="If the wielder uses a Sword, Claymore, or Polearm...",
                     image=""
                     ),
            Artifact(artifactID="golden-troupe", name="Golden Troupe", max_rarity=5,
                     two_set_bonus="Increases Elemental Skill DMG by 25%.",
                     four_set_bonus="Additionally, when not on the field...",
                     image=""
                     ),
            Artifact(artifactID="heart-of-depth", name="Heart of Depth", max_rarity=5,
                     two_set_bonus="Hydro DMG Bonus +15%",
                     four_set_bonus="After using Elemental Skill...",
                     image=""
                     ),
            Artifact(artifactID="husk-of-opulent-dreams", name="Husk of Opulent Dreams", max_rarity=5,
                     two_set_bonus="DEF +30%",
                     four_set_bonus="A character equipped with this Artifact set will obtain the Curiosity effect...",
                     image=""
                     ),
            Artifact(artifactID="instructor", name="Instructor", max_rarity=4,
                     two_set_bonus="Increases Elemental Mastery by 80.",
                     four_set_bonus="Upon triggering an Elemental Reaction...",
                     image=""
                     ),
            Artifact(artifactID="lavawalker", name="Lavawalker", max_rarity=5,
                     two_set_bonus="Pyro RES increased by 40%",
                     four_set_bonus="Increases DMG against opponents affected by Pyro...",
                     image=""
                     ),
            Artifact(artifactID="lucky-dog", name="Lucky Dog", max_rarity=3,
                     two_set_bonus="DEF increased by 100.",
                     four_set_bonus="Picking up Mora restores 300 HP.",
                     image=""
                     ),
            Artifact(artifactID="maiden-beloved", name="Maiden Beloved", max_rarity=5,
                     two_set_bonus="Healing Effectiveness +15%",
                     four_set_bonus="Using Elemental Skill or Burst increases healing...",
                     image=""
                     ),
            Artifact(artifactID="marechaussee-hunter", name="Marechaussee Hunter", max_rarity=5,
                     two_set_bonus="Normal/Charged Attack DMG +15%",
                     four_set_bonus="When current HP increases or decreases...",
                     image=""
                     ),
            Artifact(artifactID="martial-artist", name="Martial Artist", max_rarity=4,
                     two_set_bonus="Normal/Charged Attack DMG +15%",
                     four_set_bonus="After using Elemental Skill...",
                     image=""
                     ),
            Artifact(artifactID="nighttime-whispers-in-the-echoing-woods",
                     name="Nighttime Whispers in the Echoing Woods", max_rarity=5,
                     two_set_bonus="ATK +18%",
                     four_set_bonus="After using an Elemental Skill...",
                     image=""
                     ),
            Artifact(artifactID="noblesse-oblige", name="Noblesse Oblige", max_rarity=5,
                     two_set_bonus="Burst DMG +20%",
                     four_set_bonus="Using Burst increases all party members' ATK...",
                     image=""
                     ),
            Artifact(artifactID="nymphs-dream", name="Nymph's Dream", max_rarity=5,
                     two_set_bonus="Hydro DMG Bonus +15%",
                     four_set_bonus="After Normal/Charged/Plunging Attacks...",
                     image=""
                     ),
            Artifact(artifactID="ocean-hued-clam", name="Ocean-Hued Clam", max_rarity=5,
                     two_set_bonus="Healing Bonus +15%",
                     four_set_bonus="When the character heals...",
                     image=""
                     ),
            Artifact(artifactID="pale-flame", name="Pale Flame", max_rarity=5,
                     two_set_bonus="Physical DMG Bonus +25%",
                     four_set_bonus="When an Elemental Skill hits opponent...",
                     image=""
                     ),
            Artifact(artifactID="prayers-for-destiny", name="Prayers for Destiny", max_rarity=4,
                     two_set_bonus="N/A", four_set_bonus="N/A", image=""
                     ),
            Artifact(artifactID="prayers-for-illumination", name="Prayers for Illumination", max_rarity=4,
                     two_set_bonus="N/A", four_set_bonus="N/A", image=""
                     ),
            Artifact(artifactID="prayers-for-wisdom", name="Prayers for Wisdom", max_rarity=4,
                     two_set_bonus="N/A", four_set_bonus="N/A", image=""
                     ),
            Artifact(artifactID="prayers-to-springtime", name="Prayers to Springtime", max_rarity=4,
                     two_set_bonus="N/A", four_set_bonus="N/A", image=""
                     ),
            Artifact(artifactID="prayers-to-the-firmament", name="Prayers to the Firmament", max_rarity=4,
                     two_set_bonus="N/A", four_set_bonus="N/A", image=""
                     ),
            Artifact(artifactID="resolution-of-sojourner", name="Resolution of Sojourner", max_rarity=4,
                     two_set_bonus="ATK +18%",
                     four_set_bonus="Increases Charged Attack CRIT Rate...",
                     image=""
                     ),
            Artifact(artifactID="retracing-bolide", name="Retracing Bolide", max_rarity=5,
                     two_set_bonus="Shield Strength +35%",
                     four_set_bonus="While protected by a shield...",
                     image=""
                     ),
            Artifact(artifactID="scholar", name="Scholar", max_rarity=4,
                     two_set_bonus="Energy Recharge +20%",
                     four_set_bonus="Gaining Particles gives Energy...",
                     image=""
                     ),
            Artifact(artifactID="shimenawas-reminiscence", name="Shimenawa's Reminiscence", max_rarity=5,
                     two_set_bonus="ATK +18%",
                     four_set_bonus="When casting Elemental Skill...",
                     image=""
                     ),
            Artifact(artifactID="song-of-days-past", name="Song of Days Past", max_rarity=5,
                     two_set_bonus="Healing Bonus +15%",
                     four_set_bonus="When the equipping character heals someone...",
                     image=""
                     ),
            Artifact(artifactID="tenacity-of-the-millelith", name="Tenacity of the Millelith", max_rarity=5,
                     two_set_bonus="HP +20%",
                     four_set_bonus="When Elemental Skill hits opponent...",
                     image=""
                     ),
            Artifact(artifactID="the-exile", name="The Exile", max_rarity=4,
                     two_set_bonus="Energy Recharge +20%",
                     four_set_bonus="Using Burst regenerates energy...",
                     image=""
                     ),
            Artifact(artifactID="thundering-fury", name="Thundering Fury", max_rarity=5,
                     two_set_bonus="Electro DMG Bonus +15%",
                     four_set_bonus="Increases DMG from Electro reactions...",
                     image=""
                     ),
            Artifact(artifactID="thundersoother", name="Thundersoother", max_rarity=5,
                     two_set_bonus="Electro RES +40%",
                     four_set_bonus="Increases DMG against Electro-affected enemies...",
                     image=""
                     ),
            Artifact(artifactID="tiny-miracle", name="Tiny Miracle", max_rarity=4,
                     two_set_bonus="All RES +20%",
                     four_set_bonus="Incoming elemental DMG increases RES...",
                     image=""
                     ),
            Artifact(artifactID="traveling-doctor", name="Traveling Doctor", max_rarity=3,
                     two_set_bonus="Incoming healing +20%",
                     four_set_bonus="Using Burst restores HP...",
                     image=""
                     ),
            Artifact(artifactID="unfinished-reverie", name="Unfinished Reverie", max_rarity=5,
                     two_set_bonus="ATK +18%",
                     four_set_bonus="After leaving combat for 3s...",
                     image=""
                     ),
            Artifact(artifactID="vermillion-hereafter", name="Vermillion Hereafter", max_rarity=5,
                     two_set_bonus="ATK +18%",
                     four_set_bonus="After using Burst, this character gains Nascent Light...",
                     image=""
                     ),
            Artifact(artifactID="viridescent-venerer", name="Viridescent Venerer", max_rarity=5,
                     two_set_bonus="Anemo DMG Bonus +15%",
                     four_set_bonus="Increases Swirl DMG by 60%...",
                     image=""
                     ),
            Artifact(artifactID="vourukashas-glow", name="Vourukasha's Glow", max_rarity=5,
                     two_set_bonus="HP +20%",
                     four_set_bonus="Skill & Burst DMG increased...",
                     image=""
                     ),
            Artifact(artifactID="wanderers-troupe", name="Wanderer's Troupe", max_rarity=5,
                     two_set_bonus="Elemental Mastery +80",
                     four_set_bonus="Increases Charged Attack DMG...",
                     image=""
                     )
        ]

        for art in artifacts:
            art.image = f"artifact_pics/{art.artifactID}/flower-of-life.png"
            existing = db.query(Artifact).filter(Artifact.artifactID == art.artifactID).first()
            if not existing:
                db.add(art)

        db.commit()
        print(f"Successfully added {len(artifacts)} artifacts to the database.")

    except Exception as e:
        print("Error seeding artifacts:", e)
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_artifacts()
