export interface Character {
    id: number;
    key: string;
    name: string;
    title: string;
    vision: string;
    weapon: string;
    gender: string;
    nation: string;
    affiliation: string;
    rarity: number;
    release: string | null;
    constellation: string;
    birthday: string;
    description: string;
}

export interface BuildGuide {
    id: number;
    character_id: number;
    title: string;
    description: string;
    created_at: string;
    picture_path?: string;
    character?: Character;
}

export interface Upload {
    id: number;
    build_guide_id: number;
    image_path: string;
    caption: string;
    uploaded_at: string;
}

export interface User {
    id: number;
    email: string;
    role: string;
}