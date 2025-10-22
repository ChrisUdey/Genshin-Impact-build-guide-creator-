import { Character } from '@/types';

let characterMap: Record<number, Character> = {};

export function setCharacterMap(characters: Character[]) {
    characterMap = {};
    characters.forEach((char) => {
        characterMap[char.id] = char;
    });
}

export function getCharacterName(characterId: number): string {
    return characterMap[characterId]?.name || 'Unknown';
}

export function getCharacter(characterId: number): Character | undefined {
    return characterMap[characterId];
}
