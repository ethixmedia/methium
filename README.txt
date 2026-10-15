METHIUM - your matte black Spotify player

Start it
  Windows: double-click "Start Methium (Windows).bat"
  Mac:     double-click "Start Methium (Mac).command"
           (first time: right-click it, choose Open, then Open again)
  Your browser opens http://127.0.0.1:5173. Keep the small window open while listening.

First sign-in
  Click "Sign in with Spotify". Your Client ID is already filled in.
  If Spotify says the account isn't allowed, add your name and Spotify email
  under User Management in the developer dashboard.

Search tips
  /            jump to search from anywhere
  Up / Down    move through results while typing
  Enter        play the song, or open the artist/album/playlist
  Shift+Enter  add the song to your queue
  Space        play / pause
  Filters      artist, album, genre, year range, hide explicit, new albums
  You can type filters too: love artist:"atif aslam" year:2005-2012

Notes
  Needs internet and Spotify Premium. Music plays in the browser tab
  ("Methium" device) or on any other Spotify device via the devices button.
  Don't open index.html directly - always use the Start file.

Hosting on Vercel
  The repo deploys as a static site (Framework preset: Other, no build command).
  Add https://YOUR-PROJECT.vercel.app/callback to the app's Redirect URIs in the
  Spotify developer dashboard. The login screen shows the exact address to add.
