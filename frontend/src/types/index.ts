export interface Character {
    id: number;
    name: string;
    title: string;
    vision: string;
    weapon: string;
    nation: string;
    rarity: number;
    description: string;
}

export interface BuildGuide {
    id: number;
    character_id: number;
    title: string;
    description: string;
    created_at: string;
    uploads: Upload[];
}

export interface Upload {
    id: number;
    image_path: string;
    caption: string;
    uploaded_at: string;
}