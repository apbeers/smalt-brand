# How it fits together

The smalt family is one stack. Data comes in at the bottom, one engine runs everything, and each layer above it is a
different way to put that engine to work.

<EngineBar />

## Sources

Where the data lives.

- **OPFS, in your browser.** smaltdb keeps its databases in the browser's Origin Private File System, so data persists
  on the visitor's own machine.
- **External data.** Files on the web, Amazon S3 and Azure Blob Storage, read in place as external tables, through the
  [`@smaltdb/external`](/products/plugins) plugin.
- **Plugins.** Formats and sources are plugins: CSV, TSV and JSON in `@smaltdb/io`, Parquet in `@smaltdb/parquet`.
  Other people can write their own. [Plugins →](/products/plugins)

## The engine: smaltdb

One engine powers everything. smaltdb runs in a Web Worker, so the page never waits on it, and commits through a
write-ahead log, so data survives a crash. Every tool above it uses this same engine. [smaltdb →](/products/smaltdb)

## Languages: SQL and smaltdf

Two ways to tell the engine what you want, over the same tables.

- **SQL**, in a dialect that follows SQLite.
- **smaltdf**, a dataframe language in TypeScript: frames, expressions and method chains. It builds plans for the
  same engine as SQL, so a dataframe gets the same optimizer and the same storage. [smaltdf →](/products/smaltdf)

You don't need one engine for SQL tables and another for dataframes. There is one way to process your data.

## Kits

Small, focused libraries that the apps are built from: charts, tables, number formatting, the engine loader. Each kit
does one thing with few options, which keeps the apps consistent and makes them easier and more repeatable to build with
AI agents, including smaller ones. [Kits →](/products/kits)

## Apps

- **smaltui**, the SQL console, for people who live in SQL. [smaltui →](/products/smaltui)
- **smaltbi**, reports for analysts who'd rather drag a field than write a query. [smaltbi →](/products/smaltbi)
- **smaltnb**, notebooks for working through data step by step. [smaltnb →](/products/smaltnb)
