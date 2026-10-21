import * as s from "../core/validation/index.js";
import type { EnumSchema } from "../core/validation/schema.js";

/** The type of card used. */
export const CardType = {
  Visa: "visa",
  Master: "master",
  Elo: "elo",
  Cabal: "cabal",
  Alelo: "alelo",
  Discover: "discover",
  AmericanExpress: "american_express",
  Naranja: "naranja",
  DinersClub: "diners_club",
  Jcb: "jcb",
  Dankort: "dankort",
  Maestro: "maestro",
  MaestroNoLuhn: "maestro_no_luhn",
  Forbrugsforeningen: "forbrugsforeningen",
  Sodexo: "sodexo",
  Alia: "alia",
  Vr: "vr",
  Unionpay: "unionpay",
  Carnet: "carnet",
  CartesBancaires: "cartes_bancaires",
  Olimpica: "olimpica",
  Creditel: "creditel",
  Confiable: "confiable",
  Synchrony: "synchrony",
  Routex: "routex",
  Mada: "mada",
  BpPlus: "bp_plus",
  Passcard: "passcard",
  Edenred: "edenred",
  Anda: "anda",
  TarjetaD: "tarjeta-d",
  Hipercard: "hipercard",
  Bogus: "bogus",
  Switch: "switch",
  Solo: "solo",
  Laser: "laser",
} as const;
export type CardType = (typeof CardType)[keyof typeof CardType] | (string & {});

export const cardTypeSchema: EnumSchema<CardType> = s.enumOf<CardType>(CardType);
