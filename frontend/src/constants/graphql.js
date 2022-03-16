import gql from 'graphql-tag'

export const ALLE_STUKKEN_QUERY = gql`
    query AlleStukkenQuery {
        alleStukken {
          id,
          titel,
          auteur,
          genre {
            naam,
            omschrijving
          }
        }
      }
`

export const CREATE_STUK_MUTATION = gql`
      mutation CreateStukMutation($titel: String!, $auteur: String!) {
          createStuk(
              titel: $titel,
              auteur: $auteur
          ) {
              id
              titel
              auteur
          }
      }
`
