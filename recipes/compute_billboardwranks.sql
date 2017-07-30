SELECT 
    "billboard_sql"."artist" AS "artist",
    "billboard_sql"."date" AS "date",
    "billboard_sql"."rank" AS "rank",
    "billboard_sql"."song" AS "song",
    "songsranks_sql"."ranklastwk" AS "ranklastwk",
    "songsranks_sql"."ranktop" AS "ranktop",
    "songsranks_sql"."weeksonchart" AS "weeksonchart"
  FROM "JAM_billboard_sql" "billboard_sql"
  LEFT JOIN "JAM_songsranks_sql" "songsranks_sql"
    ON ("billboard_sql"."date" = "songsranks_sql"."date")
      AND ("billboard_sql"."rank" = "songsranks_sql"."rank")
      AND ("billboard_sql"."song" = "songsranks_sql"."song")