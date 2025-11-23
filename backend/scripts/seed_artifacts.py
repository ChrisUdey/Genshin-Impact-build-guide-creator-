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
            Artifact(
                artifactID="adventurer",
                name="Adventurer",
                max_rarity=3,
                two_set_bonus="Max HP increased by 1000.",
                four_set_bonus="Opening a chest regenerates 30% Max HP over 5s.",
                image=""
            ),
            Artifact(
                artifactID="archaic-petra",
                name="Archaic Petra",
                max_rarity=5,
                two_set_bonus="Geo DMG Bonus +15%",
                four_set_bonus="Upon obtaining an Elemental Shard created through a Crystallize Reaction, all party members gain 35% DMG Bonus for that particular element for 10s. Only one form of Elemental DMG Bonus can be gained in this manner at any one time.",
                image=""
            ),
            Artifact(
                artifactID="berserker",
                name="Berserker",
                max_rarity=4,
                two_set_bonus="CRIT Rate +12%",
                four_set_bonus="When HP is below 70%, CRIT Rate increases by an additional 24%.",
                image=""
            ),
            Artifact(
                artifactID="blizzard-strayer",
                name="Blizzard Strayer",
                max_rarity=5,
                two_set_bonus="Cryo DMG Bonus +15%",
                four_set_bonus="When a character attacks an opponent affected by Cryo, their CRIT Rate is increased by 20%. If the opponent is Frozen, CRIT Rate is increased by an additional 20%.",
                image=""
            ),
            Artifact(
                artifactID="bloodstained-chivalry",
                name="Bloodstained Chivalry",
                max_rarity=5,
                two_set_bonus="Physical DMG Bonus +25%",
                four_set_bonus="After defeating an opponent, increases Charged Attack DMG by 50%, and reduces its Stamina cost to 0 for 10s.",
                image=""
            ),
            Artifact(
                artifactID="brave-heart",
                name="Brave Heart",
                max_rarity=4,
                two_set_bonus="ATK +18%",
                four_set_bonus="Increases DMG by 30% against opponents with more than 50% HP.",
                image=""
            ),
            Artifact(
                artifactID="crimson-witch-of-flames",
                name="Crimson Witch of Flames",
                max_rarity=5,
                two_set_bonus="Pyro DMG Bonus +15%",
                four_set_bonus="Increases Overloaded and Burning DMG by 40%. Increases Vaporize and Melt DMG by 15%. Using an Elemental Skill increases 2-Piece Set effects by 50% for 10s. Max 3 stacks.",
                image=""
            ),
            Artifact(
                artifactID="deepwood-memories",
                name="Deepwood Memories",
                max_rarity=5,
                two_set_bonus="Dendro DMG Bonus +15%",
                four_set_bonus="After Elemental Skills or Bursts hit opponents, the targets' Dendro RES will be decreased by 30% for 8s. This effect can be triggered even if the equipping character is not on the field.",
                image=""
            ),
            Artifact(
                artifactID="defender-s-will",
                name="Defender's Will",
                max_rarity=4,
                two_set_bonus="DEF +30%",
                four_set_bonus="For each different element present in your own party, the wearer's Elemental RES to that corresponding element is increased by 30%.",
                image=""
            ),
            Artifact(
                artifactID="desert-pavilion-chronicle",
                name="Desert Pavilion Chronicle",
                max_rarity=5,
                two_set_bonus="Anemo DMG Bonus +15%",
                four_set_bonus="When Charged Attacks hit opponents, the equipping character's Normal Attack SPD will increase by 10% while Normal, Charged, and Plunging Attack DMG will increase by 40% for 15s.",
                image=""
            ),
            Artifact(
                artifactID="echoes-of-an-offering",
                name="Echoes of an Offering",
                max_rarity=5,
                two_set_bonus="ATK +18%",
                four_set_bonus="When Normal Attacks hit opponents, there is a 36% chance that it will trigger Valley Rite, which will increase Normal Attack DMG by 70% of ATK. This effect will be dispelled 0.05s after a Normal Attack deals DMG. If a Normal Attack fails to trigger Valley Rite, the odds of it triggering the next time will increase by 20%. This trigger can occur once every 0.2s.",
                image=""
            ),
            Artifact(
                artifactID="emblem-of-severed-fate",
                name="Emblem of Severed Fate",
                max_rarity=5,
                two_set_bonus="Energy Recharge +20%",
                four_set_bonus="Increases Elemental Burst DMG by 25% of Energy Recharge. A maximum of 75% bonus DMG can be obtained in this way.",
                image=""
            ),
            Artifact(
                artifactID="flower-of-paradise-lost",
                name="Flower of Paradise Lost",
                max_rarity=5,
                two_set_bonus="Elemental Mastery +80",
                four_set_bonus="The equipping character's Bloom, Hyperbloom, and Burgeon reaction DMG are increased by 40%. Additionally, after the equipping character triggers Bloom, Hyperbloom, or Burgeon, they will gain another 25% bonus to the effect mentioned prior for 10s. Each stack of this lasts independently.",
                image=""
            ),
            Artifact(
                artifactID="fragment-of-harmonic-whimsy",
                name="Fragment of Harmonic Whimsy",
                max_rarity=5,
                two_set_bonus="ATK +18%",
                four_set_bonus="When the value of a Bond of Life increases or decreases, this character deals 18% increased DMG for 6s. Max 3 stacks.",
                image=""
            ),
            Artifact(
                artifactID="gambler",
                name="Gambler",
                max_rarity=4,
                two_set_bonus="Increases Elemental Skill DMG by 20%.",
                four_set_bonus="Defeating an opponent has 100% chance to remove Elemental Skill CD. Can only occur once every 15s.",
                image=""
            ),
            Artifact(
                artifactID="gilded-dreams",
                name="Gilded Dreams",
                max_rarity=5,
                two_set_bonus="Elemental Mastery +80",
                four_set_bonus="Within 8s of triggering an Elemental Reaction, the character equipping this will obtain buffs based on the Elemental Type of the other party members. ATK is increased by 14% for each party member whose Elemental Type is the same as the equipping character, and Elemental Mastery is increased by 50 for every party member with a different Elemental Type. Each of the aforementioned buffs will count up to 3 characters. This effect can be triggered once every 8s. The character who equips this can still trigger its effects when not on the field.",
                image=""
            ),
            Artifact(
                artifactID="glacier-and-snowfield",
                name="Glacier and Snowfield",
                max_rarity=5,
                two_set_bonus="Cryo DMG Bonus +15%",
                four_set_bonus="When other nearby party members use Elemental Skills, the equipping character's CRIT DMG will be increased by 30% for 10s.",
                image=""
            ),
            Artifact(
                artifactID="gladiator-s-finale",
                name="Gladiator's Finale",
                max_rarity=5,
                two_set_bonus="ATK +18%",
                four_set_bonus="If the wielder of this artifact set uses a Sword, Claymore or Polearm, increases their Normal Attack DMG by 35%.",
                image=""
            ),
            Artifact(
                artifactID="golden-troupe",
                name="Golden Troupe",
                max_rarity=5,
                two_set_bonus="Increases Elemental Skill DMG by 25%.",
                four_set_bonus="Increases Elemental Skill DMG by 25%. Additionally, when not on the field, Elemental Skill DMG will be further increased by 25%. This effect will be cleared 2s after taking the field.",
                image=""
            ),
            Artifact(
                artifactID="heart-of-depth",
                name="Heart of Depth",
                max_rarity=5,
                two_set_bonus="Hydro DMG Bonus +15%",
                four_set_bonus="After using Elemental Skill, increases Normal Attack and Charged Attack DMG by 30% for 15s.",
                image=""
            ),
            Artifact(
                artifactID="husk-of-opulent-dreams",
                name="Husk of Opulent Dreams",
                max_rarity=5,
                two_set_bonus="DEF +30%",
                four_set_bonus="A character equipped with this Artifact set will obtain the Curiosity effect in the following conditions: When on the field, the character gains 1 stack after hitting an opponent with a Geo attack, triggering a maximum of once every 0.3s. When off the field, the character gains 1 stack every 3s. Curiosity can stack up to 4 times, each providing 6% DEF and a 6% Geo DMG Bonus. When 6 seconds pass without gaining a Curiosity stack, 1 stack is lost.",
                image=""
            ),
            Artifact(
                artifactID="instructor",
                name="Instructor",
                max_rarity=4,
                two_set_bonus="Increases Elemental Mastery by 80.",
                four_set_bonus="Upon triggering an Elemental Reaction, increases all party members' Elemental Mastery by 120 for 8s.",
                image=""
            ),
            Artifact(
                artifactID="lavawalker",
                name="Lavawalker",
                max_rarity=5,
                two_set_bonus="Pyro RES increased by 40%",
                four_set_bonus="Increases DMG against opponents affected by Pyro by 35%.",
                image=""
            ),
            Artifact(
                artifactID="lucky-dog",
                name="Lucky Dog",
                max_rarity=3,
                two_set_bonus="DEF increased by 100.",
                four_set_bonus="Picking up Mora restores 300 HP.",
                image=""
            ),
            Artifact(
                artifactID="maiden-beloved",
                name="Maiden Beloved",
                max_rarity=5,
                two_set_bonus="Character Healing Effectiveness +15%",
                four_set_bonus="Using an Elemental Skill or Burst increases healing received by all party members by 20% for 10s.",
                image=""
            ),
            Artifact(
                artifactID="marechaussee-hunter",
                name="Marechaussee Hunter",
                max_rarity=5,
                two_set_bonus="Normal and Charged Attack DMG +15%",
                four_set_bonus="When current HP increases or decreases, CRIT Rate will be increased by 12% for 5s. Max 3 stacks.",
                image=""
            ),
            Artifact(
                artifactID="martial-artist",
                name="Martial Artist",
                max_rarity=4,
                two_set_bonus="Normal and Charged Attack DMG +15%",
                four_set_bonus="After using Elemental Skill, increases Normal Attack and Charged Attack DMG by 25% for 8s.",
                image=""
            ),
            Artifact(
                artifactID="nighttime-whispers-in-the-echoing-woods",
                name="Nighttime Whispers in the Echoing Woods",
                max_rarity=5,
                two_set_bonus="ATK +18%",
                four_set_bonus="After using an Elemental Skill, gain a 20% Geo DMG Bonus for 10s. While under a shield granted by the Crystallize reaction, the above effect will be increased by 150%, and this additional increase disappears 1s after that shield is lost.",
                image=""
            ),
            Artifact(
                artifactID="noblesse-oblige",
                name="Noblesse Oblige",
                max_rarity=5,
                two_set_bonus="Elemental Burst DMG +20%",
                four_set_bonus="Using an Elemental Burst increases all party members' ATK by 20% for 12s. This effect cannot stack.",
                image=""
            ),
            Artifact(
                artifactID="nymph-s-dream",
                name="Nymph's Dream",
                max_rarity=5,
                two_set_bonus="Hydro DMG Bonus +15%",
                four_set_bonus="After Normal, Charged, and Plunging Attacks, Elemental Skills, and Elemental Bursts hit opponents, 1 stack of Mirrored Nymph will be triggered, lasting 8s. When under the effect of 1, 2, or 3 or more Mirrored Nymph stacks, ATK will be increased by 7%/16%/25%, and Hydro DMG Bonus will be increased by 4%/9%/15%. Mirrored Nymph stacks created by Normal, Charged, and Plunging Attacks, Elemental Skills, and Elemental Bursts exist independently.",
                image=""
            ),
            Artifact(
                artifactID="ocean-hued-clam",
                name="Ocean-Hued Clam",
                max_rarity=5,
                two_set_bonus="Healing Bonus +15%",
                four_set_bonus="When the character equipping this artifact set heals a character in the party, a Sea-Dyed Foam will appear for 3s, accumulating the amount of HP recovered from healing (including overflow healing). At the end of the duration, the Sea-Dyed Foam will explode, dealing DMG to nearby opponents based on 90% of the accumulated healing. (This DMG is calculated similarly to Reactions such as Electro-Charged, and Superconduct, but is not affected by Elemental Mastery, Character Levels, or Reaction DMG Bonuses). Only one Sea-Dyed Foam can be produced every 3.5s. Each Sea-Dyed Foam can accumulate up to 30,000 HP (including overflow healing). There can be no more than one Sea-Dyed Foam active at any given time. This effect can still be triggered even when the character who is using this artifact set is not on the field.",
                image=""
            ),
            Artifact(
                artifactID="pale-flame",
                name="Pale Flame",
                max_rarity=5,
                two_set_bonus="Physical DMG Bonus +25%",
                four_set_bonus="When an Elemental Skill hits an opponent, ATK is increased by 9% for 7s. This effect stacks up to 2 times and can be triggered once every 0.3s. Once 2 stacks are reached, the 2-set effect is increased by 100%.",
                image=""
            ),
            Artifact(
                artifactID="prayers-for-destiny",
                name="Prayers for Destiny",
                max_rarity=4,
                two_set_bonus="N/A",
                four_set_bonus="N/A",
                image=""
            ),
            Artifact(
                artifactID="prayers-for-illumination",
                name="Prayers for Illumination",
                max_rarity=4,
                two_set_bonus="N/A",
                four_set_bonus="N/A",
                image=""
            ),
            Artifact(
                artifactID="prayers-for-wisdom",
                name="Prayers for Wisdom",
                max_rarity=4,
                two_set_bonus="N/A",
                four_set_bonus="N/A",
                image=""
            ),
            Artifact(
                artifactID="prayers-to-springtime",
                name="Prayers to Springtime",
                max_rarity=4,
                two_set_bonus="N/A",
                four_set_bonus="N/A",
                image=""
            ),
            Artifact(
                artifactID="prayers-to-the-firmament",
                name="Prayers to the Firmament",
                max_rarity=4,
                two_set_bonus="N/A",
                four_set_bonus="N/A",
                image=""
            ),
            Artifact(
                artifactID="resolution-of-sojourner",
                name="Resolution of Sojourner",
                max_rarity=4,
                two_set_bonus="ATK +18%",
                four_set_bonus="Increases Charged Attack CRIT Rate by 30%.",
                image=""
            ),
            Artifact(
                artifactID="retracing-bolide",
                name="Retracing Bolide",
                max_rarity=5,
                two_set_bonus="Increases Shield Strength by 35%.",
                four_set_bonus="While protected by a shield, gain an additional 40% Normal and Charged Attack DMG.",
                image=""
            ),
            Artifact(
                artifactID="scholar",
                name="Scholar",
                max_rarity=4,
                two_set_bonus="Energy Recharge +20%",
                four_set_bonus="Gaining Elemental Particles or Orbs gives 3 Energy to all party members who have a bow or a catalyst equipped. Can only occur once every 3s.",
                image=""
            ),
            Artifact(
                artifactID="shimenawa-s-reminiscence",
                name="Shimenawa's Reminiscence",
                max_rarity=5,
                two_set_bonus="ATK +18%",
                four_set_bonus="When casting an Elemental Skill, if the character has 15 or more Energy, they lose 15 Energy and Normal/Charged/Plunging Attack DMG is increased by 50% for 10s. This effect will not trigger again during that duration.",
                image=""
            ),
            Artifact(
                artifactID="song-of-days-past",
                name="Song of Days Past",
                max_rarity=5,
                two_set_bonus="Healing Bonus +15%",
                four_set_bonus="When the equipping character heals a party member, the Yearning effect will be created for 6s, which records the total amount of healing provided (including overflow healing). When the duration expires, the Yearning effect will be transformed into the Waves of Days Past effect: When your active party member hits an opponent with a Normal Attack, Charged Attack, Plunging Attack, Elemental Skill, or Elemental Burst, the DMG dealt will be increased by 8% of the total healing amount recorded by the Yearning effect. The Waves of Days Past effect is removed after it has taken effect 5 times or after 10s. A single instance of the Yearning effect can record up to 15,000 healing, and only a single instance can exist at once, but it can record the healing from multiple equipping characters. Equipping characters on standby can still trigger this effect.",
                image=""
            ),
            Artifact(
                artifactID="tenacity-of-the-millelith",
                name="Tenacity of the Millelith",
                max_rarity=5,
                two_set_bonus="HP +20%",
                four_set_bonus="When an Elemental Skill hits an opponent, the ATK of all nearby party members is increased by 20% and their Shield Strength is increased by 30% for 3s. This effect can be triggered once every 0.5s. This effect can still be triggered even when the character who is using this artifact set is not on the field.",
                image=""
            ),
            Artifact(
                artifactID="the-exile",
                name="The Exile",
                max_rarity=4,
                two_set_bonus="Energy Recharge +20%",
                four_set_bonus="Using an Elemental Burst regenerates 2 Energy for all party members (excluding the wearer) every 2s for 6s. This effect cannot stack.",
                image=""
            ),
            Artifact(
                artifactID="thundering-fury",
                name="Thundering Fury",
                max_rarity=5,
                two_set_bonus="Electro DMG Bonus +15%",
                four_set_bonus="Increases DMG caused by Overloaded, Electro-Charged, Superconduct, and Hyperbloom by 40%, and the DMG Bonus conferred by Aggravate is increased by 20%. When Quicken or the aforementioned Elemental Reactions are triggered, Elemental Skill CD is decreased by 1s. Can only occur once every 0.8s.",
                image=""
            ),
            Artifact(
                artifactID="thundersoother",
                name="Thundersoother",
                max_rarity=5,
                two_set_bonus="Electro RES increased by 40%",
                four_set_bonus="Increases DMG against opponents affected by Electro by 35%.",
                image=""
            ),
            Artifact(
                artifactID="tiny-miracle",
                name="Tiny Miracle",
                max_rarity=4,
                two_set_bonus="All Elemental RES increased by 20%.",
                four_set_bonus="Incoming Elemental DMG increases corresponding Elemental RES by 30% for 10s. Can only occur once every 10s.",
                image=""
            ),
            Artifact(
                artifactID="traveling-doctor",
                name="Traveling Doctor",
                max_rarity=3,
                two_set_bonus="Increases incoming healing by 20%.",
                four_set_bonus="Using Elemental Burst restores 20% HP.",
                image=""
            ),
            Artifact(
                artifactID="unfinished-reverie",
                name="Unfinished Reverie",
                max_rarity=5,
                two_set_bonus="ATK +18%",
                four_set_bonus="After leaving combat for 3s, DMG dealt is increased by 50%. In combat, if no Burning opponents are nearby for more than 6s, this DMG Bonus will decrease by 10% per second until it reaches 0%. When a Burning opponent exists, the DMG Bonus will increase by 10% per second until it reaches 50%. This effect still triggers if the equipping character is off-field.",
                image=""
            ),
            Artifact(
                artifactID="vermillion-hereafter",
                name="Vermillion Hereafter",
                max_rarity=5,
                two_set_bonus="ATK +18%",
                four_set_bonus="After using an Elemental Burst, this character will gain the Nascent Light effect, increasing their ATK by 8% for 16s. When the character's HP decreases, their ATK will further increase by 10%. This increase can occur this way maximum of 4 times. This effect can be triggered once every 0.8s. Nascent Light will be dispelled when the character leaves the field. If an Elemental Burst is used again during the duration of Nascent Light, the original Nascent Light will be dispelled.",
                image=""
            ),
            Artifact(
                artifactID="viridescent-venerer",
                name="Viridescent Venerer",
                max_rarity=5,
                two_set_bonus="Anemo DMG Bonus +15%",
                four_set_bonus="Increases Swirl DMG by 60%. Decreases opponent's Elemental RES to the element infused in the Swirl by 40% for 10s.",
                image=""
            ),
            Artifact(
                artifactID="vourukasha-s-glow",
                name="Vourukasha's Glow",
                max_rarity=5,
                two_set_bonus="HP +20%",
                four_set_bonus="Elemental Skill and Elemental Burst DMG will be increased by 10%. After the equipping character takes DMG, the aforementioned DMG Bonus is increased by 80% for 5s. This effect increase can have 5 stacks. The duration of each stack is counted independently. These effects can be triggered even when the equipping character is not on the field.",
                image=""
            ),
            Artifact(
                artifactID="wanderer-s-troupe",
                name="Wanderer's Troupe",
                max_rarity=5,
                two_set_bonus="Increases Elemental Mastery by 80.",
                four_set_bonus="Increases Charged Attack DMG by 35% if the character uses a Catalyst or Bow.",
                image=""
            ),
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
