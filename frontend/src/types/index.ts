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
    username: string;
    id: number;
    character_name: string;
    character_id: number;
    title: string;
    description: string;
    created_at: string;
    picture_path?: string;
    character?: Character;
}

export interface Artifact {
    id: string;
    name: string;
    max_rarity: number;
    two_set_bonus: string;
    four_set_bonus: string;
    image: string;
}

export interface DomainArtifact {
    id: number;
    artifact_id: string;
    artifact: Artifact;
}

export interface Domain {
    id: number;
    name: string;
    type: string;
    description: string;
    location: string;
    nation: string;
    picture_path: string;
    artifacts: DomainArtifact[];
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