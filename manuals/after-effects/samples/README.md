# Original offline practice assets

These small assets were authored for this manual. They are original examples, supplied under CC0-1.0; reuse and modify them freely. They contain no Adobe assets or third-party fonts.

- `badge.svg`: a simple icon with paths and fills, no text. Import as footage and as a composition to compare linked pixels and editable shapes. Inspect the three colored parts after conversion.
- `stats.json`: `{"team":"North","score":42}`. Import into AE; on Source Text use `String(footage("stats.json").sourceData.score);`. Change the file and Reload Footage to test updates.
- `characters.csv`: a header and three rows. Import as data; add to a test comp, expand Data and use the pick whip to obtain the actual `dataValue(...)` cell path. Confirm against the table; do not guess the row/column path from a nested JSON example.
- `pulse.wav`: four seconds, 48 kHz mono 16-bit PCM, with short 440 Hz pulses once a second. Use for manual markers, waveform inspection and Convert Audio to Keyframes. It is a synthetic signal, not speech or a calibration standard.

Generate other exercise material inside AE: solids, shape paths, text, grids, noise and native meshes. Tracking, camera-solving, keying and Object Matte require suitable footage: record a short moving object/person or use footage you may lawfully use. A generated card is sufficient for transform practice but does not validate a photographic tracking/keying exercise. Variable-font work needs an installed variable font; SBSAR practice needs a material obtained before going offline. The reader itself needs neither.
