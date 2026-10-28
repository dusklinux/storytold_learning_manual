"""Editorial second-pass corrections and supplements for the 27.11 Windows edition.

The overrides deliberately execute before derived website/Markdown/CSV generation.
Evidence boundaries are described in AUDIT_SECOND_PASS.md.
"""

def patch(LESSONS, TOOLS, FILTERS, SHORTCUTS, GLOSSARY, TROUBLE, RECIPES):
    byid={x['id']:x for x in LESSONS}
    # Correct actual order of instructions and improve reproducibility.
    x=byid['s01l01'];x['steps'][1]='Select Brush Tool (B), create a blank pixel layer, click once with a hard brush, then zoom to 400% to inspect the painted pixel edge.'
    x=byid['s03l05'];x['location']='Quick Mask Mode button in Toolbar or Q; Select > Save Selection; Window > Channels'
    x=byid['s03l02'];x['location']='Object Selection Tool (W group); Quick Selection Tool (W group); Selection Brush Tool (L group); Select > Color Range'
    x=byid['s03l02'];x['tip']='Use the Selection Brush (L tool group) for painted selection refinement when available; do not confuse its overlay with a persistent layer mask.'
    x=byid['s08l04'];x['location']='File > Open (select a supported camera RAW file); Filter > Camera Raw Filter; Help > About Plug-In > Camera Raw'
    x=byid['s10l05'];x['location']='File > Export > Export As; File > Export > Quick Export (output format follows Export preferences)'
    x=byid['s11l06'];x['location']='Help > About Photoshop; Edit > Preferences > Performance; Creative Cloud desktop account/subscription information'
    x=byid['s02l03'];x['mistake']='Alignment and Distribute require the correct target layers, selection and sometimes an explicit reference; check the Options bar before assuming they will operate.'
    x=byid['s10l04'];x['tip']='Prefer Actions for simple repeatable editing; Adobe UXP plug-ins and Photoshop scripting are different extension methods with distinct support and security constraints.'
    x=byid['s03l04'];x['tip']='Inspect both light and dark backgrounds. Enhance edge is a version-specific, AI-assisted option; availability and processing requirements are not a promise of offline use.'
    x=byid['s05l03'];x['tip']='Choose Remove processing mode deliberately: on-device requires an available locally downloaded model and suitable hardware; cloud processing requires service access. Confirm labels in 27.11.'
    # Cross-stage prerequisites are informative, never navigation gates.
    extra={
      's03l03':['s02l02','s02l04'], 's03l04':['s03l02','s03l03'],
      's03l06':['s02l02','s03l03'], 's04l03':['s04l02'],
      's05l04':['s03l03','s04l01'], 's05l05':['s04l01','s03l03'],
      's06l05':['s03l03'], 's07l05':['s07l01','s07l04'],
      's08l04':['s04l02'], 's08l06':['s08l05'],
      's09l01':['s03l03','s04l02','s08l02'],
      's09l02':['s09l01','s04l03'],
      's09l05':['s04l02','s07l04'],
      's09l06':['s05l04','s08l05'],
      's10l02':['s01l03','s02l01'],
      's10l05':['s02l04','s08l05'],
      's11l02':['s11l01'],
      's12l06':['s09l07','s10l02','s10l05','s11l05']}
    for lid,preds in extra.items():
        x=byid[lid]
        for p in preds:
            if p not in x['prerequisites']:x['prerequisites'].append(p)
    # Common tool defaults: K is Frame, R is Rotate View. Blur/Sharpen/Smudge have
    # no trustworthy current default letter: old K lists pre-date Frame.
    for t in TOOLS:
        if t['title'] in ('Blur','Sharpen','Smudge'):t['shortcut']=''
        if t['title']=='Artboard':t['shortcut']='V'
        if t['title']=='Selection Brush':t['shortcut']='L'
    TOOLS[:]=[t for t in TOOLS if t['title']!='Color Sampler and measuring tools'] # duplicated group, not a unique tool
    TOOLS.append(dict(title='Adjustment Brush',family='Local adjustments',shortcut='B',purpose='Paints the coverage of a non-destructive local adjustment while adjusting image tone or color.',controls='Adjustment type; brush size; hardness; Add/Subtract; properties vary',use='Make local reversible correction without manually creating the mask first.',caution='Verify that the adjustment mask, not source pixels, is selected and account for the current Tool group.',lesson='s04l01'))
    # Make each tool's toolbar location useful, rather than repeating a generic
    # "somewhere in the Toolbar" reference 71 times. Tool grouping may be customized.
    tool_groups={
        'V':'Move/Artboard','K':'Frame','M':'Marquee','L':'Lasso/Selection Brush',
        'W':'Object/Quick Selection/Magic Wand','C':'Crop/Slice',
        'I':'Eyedropper/Measurement','J':'Healing/Remove','B':'Brush/Adjustment Brush',
        'S':'Stamp','Y':'History Brush','E':'Eraser','G':'Gradient/Paint Bucket',
        'O':'Dodge/Burn/Sponge','P':'Pen','A':'Path/Direct Selection',
        'T':'Type','U':'Shape','H':'Hand','R':'Rotate View','Z':'Zoom'}
    for t in TOOLS:
        # These are grouped under the nearest listed keyboard family, but do
        # not silently assign a default shortcut where one does not exist.
        group=tool_groups.get(t['shortcut']) if t['shortcut'] else None
        if not group:
            if t['title'] in ('Single Row Marquee','Single Column Marquee'):group='Marquee'
            elif t['title'] in ('Add Anchor Point','Delete Anchor Point','Convert Point'):group='Pen'
            elif t['title'] in ('Blur','Sharpen','Smudge'):group='Blur/Sharpen/Smudge'
            else:group=t['title']
        t['location']=f'Toolbar > {group} tool group (expand the tool group; Edit > Toolbar if not visible)'
    # Fix filter menu paths, including commands incorrectly categorized as Filter.
    locations={
      'Field Blur':'Filter > Blur Gallery > Field Blur','Iris Blur':'Filter > Blur Gallery > Iris Blur',
      'Tilt-Shift':'Filter > Blur Gallery > Tilt-Shift','Path Blur':'Filter > Blur Gallery > Path Blur',
      'Spin Blur':'Filter > Blur Gallery > Spin Blur',
      'Liquify':'Filter > Liquify', 'Perspective Warp':'Edit > Perspective Warp',
      'Camera Raw Filter':'Filter > Camera Raw Filter','Lens Correction':'Filter > Lens Correction',
      'Vanishing Point':'Filter > Vanishing Point',
      'High Pass':'Filter > Other > High Pass','Maximum':'Filter > Other > Maximum',
      'Minimum':'Filter > Other > Minimum','Offset':'Filter > Other > Offset',
      'Neural Filters':'Filter > Neural Filters',
      'AI Sharpen (Topaz)':'Filter > AI Sharpen (premium cloud service; eligibility and credits required)',
      'AI Denoise (Topaz)':'Filter > AI Denoise (premium cloud service; eligibility and credits required)',
      'Shake Reduction':'REMOVED in Photoshop 23.3 (historical: Filter > Sharpen > Shake Reduction)'}
    for f in FILTERS:
        if f['title'] in locations:f['location']=locations[f['title']]
        if f['title'] in ('Lens Blur','Flame','Tree','Vanishing Point'):
            f['caution']+=' Not available as an editable Smart Filter in Adobe’s Oct 2026 Smart Filter documentation.'
        if f['title']=='Neural Filters':f['caution']+=' Some models require a download or an online service; do not assume the same offline requirements for all.'
        if f['title']=='Shake Reduction':
            f['status']='REMOVED in 23.3; legacy reference only, unavailable in 27.11'
            f['caution']='Removed starting in Photoshop 23.3 (April 2022); do not attempt this historical command in 27.11. Use contemporary non-destructive sharpening or qualifying AI methods instead. Adobe documentation confirms the removal.'
        if f['title'] in ('AI Sharpen (Topaz)','AI Denoise (Topaz)'):
            f['caution']+=' This premium service operates on the active layer with no new layer; duplicate the original first. Adobe documents a 56 MP file cap and usage-credit charges (verify current entitlement/terms).'
    # Purge a duplicate/misleading F entry; replace misleading R with no default
    # and independently documented K (Frame). Keys are context-sensitive.
    SHORTCUTS[:]=[s for s in SHORTCUTS if s['action'] not in ('Full screen menus varies','Blur/Sharpen/Smudge')]
    for s in SHORTCUTS:
        if s['action']=='Rotate View':s['note']='R selects Rotate View, not Blur. Document view only; GPU support may affect operation.'
        if s['action']=='Selection family':s['note']='Object Selection, Quick Selection and Magic Wand are W-group; Selection Brush is in the L group.'
        if s['action']=='Brush':s['note']='B includes Brush and may cycle to Adjustment Brush; default keyboard focus and tool set matter.'
        if s['action']=='Zoom in':s['keys']='Ctrl++ (plus)'
    additions=[
      ('Tools','Frame Tool','K','Tool','Current Frame Tool default; historical Blur K listings are obsolete.'),
      ('Tools','Artboard tool','V','Tool','Grouped with Move; use the tool-group cycle or toolbar.'),
      ('Tools','Selection Brush tool','L','Tool','Grouped with Lasso in modern Photoshop; use group cycle.'),
      ('Tools','Adjustment Brush tool','B','Tool','Modern adjustment family grouped with Brush; toolbar configuration may vary.'),
      ('Tools','Blur/Sharpen/Smudge tools','No default key','Tool','Do NOT use R (Rotate View) or K (Frame); access the toolbar or assign custom shortcut.'),
      ('Editing','Copy','Ctrl+C','Document/selection','Standard copy; may copy selected pixel content or object.'),
      ('Editing','Cut','Ctrl+X','Document/selection','Changes pixels or content depending on selection.'),
      ('Editing','Paste','Ctrl+V','Document/selection','Creates/imports pasted content as appropriate.'),
      ('Editing','Copy Merged','Ctrl+Shift+C','Active pixel selection','Copies composite visible pixels rather than one layer.'),
      ('Editing','Paste in Place','Ctrl+Shift+V','Document','Positioned paste; document/clipboard context matters.'),
      ('Editing','Fill dialog','Shift+F5','Document/selection','Application command; menu can also open fill.'),
      ('Editing','Color Settings','Ctrl+Shift+K','Global','Adobe Windows desktop command; changes color management preferences.'),
      ('Editing','Export As','Ctrl+Alt+Shift+W','Document','Legacy Adobe shortcut reference; verify 27.11 shortcut menu.'),
      ('Editing','Save for Web (Legacy)','Ctrl+Alt+Shift+S','Document','Legacy path; may be hidden in recent versions.'),
      ('Editing','Revert to last saved','F12','Document','Discards subsequent edits; use only after saving copies.'),
      ('Editing','Quit Photoshop','Ctrl+Q','Global','Offers save prompts for changed documents.'),
      ('Layer','Create layer via cut','Ctrl+Shift+J','Active selection','Creates a new layer from selected pixels where applicable.'),
      ('Layer','Merge selected layers','Ctrl+E','Selected layers','Destructive; preserve layered master.'),
      ('Layer','Merge visible','Ctrl+Shift+E','Document','Destructive; save layered working file first.'),
      ('Layer','Stamp visible on new layer','Ctrl+Alt+Shift+E','Document','Merges a snapshot of visible layers onto a new layer; verify active target.'),
      ('Layer','Clip to layer below','Ctrl+Alt+G','Layers panel','Create/release clipping mask; needs suitable base layer.'),
      ('Selection','Select pixels from layer thumbnail','Ctrl+click layer thumbnail','Layers panel mouse gesture','Loads layer transparency as a selection.'),
      ('Selection','Temporarily add to selection','Shift+drag','Selection tool gesture','Add selection area while the tool is active.'),
      ('Selection','Temporarily subtract from selection','Alt+drag','Selection tool gesture','Subtract selected area while the tool is active.'),
      ('Selection','Intersect with selection','Shift+Alt+drag','Selection tool gesture','Intersection of new and existing selections.'),
      ('Masks','View layer mask alone','Alt+click mask thumbnail','Layers panel mouse gesture','Toggle grayscale mask-only view.'),
      ('Masks','Disable/enable layer mask','Shift+click mask thumbnail','Layers panel mouse gesture','Temporarily bypass mask; red X marker shows disabled state.'),
      ('Masks','Duplicate mask to another layer','Alt+drag mask thumbnail','Layers panel mouse gesture','Copies mask, leaving original attached.'),
      ('Masks','Solo layer visibility','Alt+click eye icon','Layers panel mouse gesture','Restoration can be affected if you change other layer visibilities while isolated.'),
      ('View','Zoom temporarily in','Ctrl+Space (hold)','Canvas gesture','May interact with Windows keyboard/layout and other tools.'),
      ('View','Zoom temporarily out','Alt+Space (hold)','Canvas gesture','May conflict with Windows system menu in some environments.'),
      ('View','Fit view to screen via Hand tool','Double-click Hand Tool','Toolbar mouse gesture','Shows entire document in available viewport.'),
      ('View','100% view via Zoom tool','Double-click Zoom Tool','Toolbar mouse gesture','Useful for assessing real pixel sharpness.'),
      ('Painting','Previous brush preset',',','Brush tool','Preset order and active brush tool determine behavior.'),
      ('Painting','Next brush preset','.','Brush tool','Preset order and active brush tool determine behavior.'),
      ('Painting','Temporarily erase with same brush tip','~ (hold)','Brush tool','Switches brush to eraser mode on supported modern Photoshop setups.'),
      ('Painting','Lock/unlock transparent pixels','/','Layers panel','Applies to appropriate pixel layer and context; can vary with keyboard layout.'),
      ('Panels','Brush Settings panel','F5','Global/panel','Function keys may be intercepted by keyboard firmware or OS.'),
      ('Panels','Color panel','F6','Global/panel','Function keys may be intercepted by keyboard firmware or OS.'),
      ('Panels','Layers panel','F7','Global/panel','Function keys may be intercepted by keyboard firmware or OS.'),
      ('Panels','Info panel','F8','Global/panel','Function keys may be intercepted by keyboard firmware or OS.'),
      ('Panels','Actions panel','F9','Global/panel','Function keys may be intercepted by keyboard firmware or OS.'),
      ('Filters','Liquify workspace','Ctrl+Shift+X','Document','GPU requirements, layer types and active document can prevent command.'),
      ('Layer','Nudge selected content 1 pixel','Arrow key','Move Tool/transform','Depends on selected layer/selection and active text input.'),
      ('Layer','Nudge selected content 10 pixels','Shift+Arrow key','Move Tool/transform','Depends on selected layer/selection and active text input.'),
    ]
    existing={(x['action'].lower(),x['keys'].lower()) for x in SHORTCUTS}
    for family,action,keys,context,note in additions:
        if (action.lower(),keys.lower()) not in existing:
            SHORTCUTS.append(dict(family=family,action=action,keys=keys,context=context,note=note))
    # Additional glossary terms that fill actionable beginner/production gaps.
    for term,definition,lesson in [
      ('Brush spacing','Distance between individual brush-tip imprints; smaller spacing generally produces smoother continuous strokes.','s06l01'),
      ('Brush jitter','Controlled randomness in size, angle, position or color of repeated brush marks.','s06l02'),
      ('ICC rendering intent','Rule for mapping colors between gamuts during a conversion, especially perceptual versus relative colorimetric.','s08l06'),
      ('Soft proof','A color-managed on-screen preview of how a destination output profile may reproduce an image.','s08l06'),
      ('Smart Filter stacking','Order of filters attached to Smart Objects; changing order can change the final image.','s04l03'),
      ('Clipped adjustment','An adjustment constrained by the underlying layer or clip base, distinct from masking by painted gray values.','s04l01'),
      ('Alpha lock','Prevents painting into fully transparent areas on supported raster layers.','s02l04'),
      ('Generative credits','Usage accounting for eligible cloud-based AI operations; entitlement may differ by plan, region and model.','s11l06'),
      ('UXP','Adobe Unified Extensibility Platform for supported Photoshop modern plug-ins and scripting integrations.','s10l04'),
      ('Scratch disk','Disk space used to extend working memory and store temporary data for demanding Photoshop operations.','s11l01'),
      ('Export preflight','Final inspection of dimensions, color profile, transparency, filenames and deliverable requirements.','s10l05')]:
        if not any(g['term']==term for g in GLOSSARY):GLOSSARY.append(dict(term=term,definition=definition,lesson=lesson))
    # New recipes; no new learning prerequisites needed.
    for title,requires,procedure,passed in [
      ('Make a reversible crop',['s02l01'],'Select Crop Tool; disable Delete Cropped Pixels; commit; inspect outside frame by expanding crop; keep a layered master.','Original crop area can be recovered before final delivery.'),
      ('Clean a mask fringe',['s03l03','s03l04'],'Place subject against white and black layers; open Select and Mask; try restrained edge refinement and Decontaminate Colors only when outputting safely to a separate result; inspect at 100%.','Edges remain clean on both backgrounds with original mask retained.'),
      ('Build controlled rim lighting',['s04l01','s05l05'],'Create a Curves brighten adjustment, invert mask to black, paint a low-flow soft white edge on subject side and adjust opacity.','Lighting direction is consistent and no harsh white outline appears.'),
      ('Create multiple editable artboard sizes',['s02l02','s10l05'],'Create artboards for distinct delivery sizes; reuse linked Smart Objects and text; inspect each trim independently; export artboards per output constraints.','Each exported variant has expected dimensions and editable text in the master.'),
      ('Check missing linked assets',['s04l02','s10l01'],'Inspect Layers for warning icons; check File > Package where available; duplicate project folder and reopen; relink from included source folder.','Transferred project opens with the intended original linked graphics.'),
      ('Verify a transparent export',['s02l04','s10l05'],'Hide all opaque background layers; use Export As > PNG with transparency; reopen against dark and light backgrounds.','No white rectangular matte or unwanted halo remains.'),
      ('Inspect two different ICC previews',['s08l05','s08l06'],'Preserve RGB master; set destination in View > Proof Setup > Custom; toggle Proof Colors; compare with profile embedded in final exported copy.','Report identifies soft-proof profile and documents visible changes without overwriting master.'),
      ('Compare blur as Smart Filter and raster edit',['s04l02','s04l03'],'Duplicate an image layer; convert one copy to Smart Object and apply Gaussian Blur; blur other raster copy directly; close and reopen PSD; try editing both.','Smart Filter settings remain separately adjustable; direct blur is baked into raster pixels.'),
      ('Inspect a suspicious keyboard shortcut',['s01l04','s11l03'],'Open Edit > Keyboard Shortcuts (Ctrl+Alt+Shift+K); choose Tools or Application Menus; record exact assigned key; compare with manual and look for user customization.','Report distinguishes installed assignment from historical or documented default.'),
      ('Separate AI-generated and recovered content',['s05l07','s11l06'],'Save archival original; keep AI-assisted reconstruction on a named layer; label uncertain invented detail; include original plus change log in handoff.','A reviewer can see which regions were authentically preserved and which were inferred.')]:
        if not any(r['title']==title for r in RECIPES): RECIPES.append(dict(title=title,requires=requires,procedure=procedure,pass_=passed) if False else {'title':title,'requires':requires,'procedure':procedure,'pass':passed})

    # Replace boilerplate practical-use text with skill-specific production scenarios.
    uses={
    's01l01':'Use this distinction when choosing Photoshop raster editing versus editable shape/type artwork for logos, graphics and photographs.',
    's01l02':'Use these measurements when preparing screen assets and calculating native-size photographic prints without inventing image detail.',
    's01l03':'Use a layered master plus separate delivery files whenever a client may request revisions after an export.',
    's01l04':'Use a consistent workspace when switching between retouching, compositing and layout without altering document content.',
    's01l05':'Use 100% zoom for pixel judgment and guides/rulers for repeatable spacing before export.',
    's01l06':'Use History for immediate experiments, but save versioned PSDs before risky reconstruction or filters.',
    's02l01':'Use crop, canvas size and image size as separate choices for framing, adding space and changing resolution.',
    's02l02':'Use descriptive layer names and groups when a multi-element design must be handed to someone else.',
    's02l03':'Use alignment/distribution and numeric transforms for tiled layouts, badges and systematic mockups.',
    's02l04':'Use alpha transparency for logos, stickers, overlays and icons that must sit on varied backgrounds.',
    's02l05':'Use live layer styles for reusable outlined text, subtle shadows and brand-consistent interface graphics.',
    's02l06':'Use Smart Guides and grid snapping where repeated margins and exact alignment matter more than visual guesswork.',
    's03l01':'Use geometric selections for bounded fills, crops and controlled local pixel operations.',
    's03l02':'Use a selection method matched to object shape, edge contrast and color complexity before refining a mask.',
    's03l03':'Use a layer mask wherever temporary isolation, retouch restraint or revision-friendly concealment is required.',
    's03l04':'Use Select and Mask for hair, soft edges and contrast-dependent composites that must work on multiple backgrounds.',
    's03l05':'Use saved selection channels when the same complex region needs several separate corrections later.',
    's03l06':'Use clipping masks for content inside editable letters/shapes and vector masks for crisp geometric reveal boundaries.',
    's04l01':'Use adjustment layers when tonal or color changes need client-review toggles and separately controlled masks.',
    's04l02':'Use embedded Smart Objects for portable components; use linked sources when shared artwork must update in multiple files.',
    's04l03':'Use Smart Filters when sharpening or blur settings must remain adjustable after saving and reopening.',
    's04l04':'Use blend modes and Fill/Opacity controls for realistic shadow, highlight and special-effect layer composites.',
    's04l05':'Use Blend If to reveal underlying texture/luminance without permanently deleting or painting source pixels.',
    's04l06':'Use versioned working documents and named adjustments for accountable client revisions and team handoffs.',
    's05l01':'Use healing on small skin marks, dust and sensor spots where the surrounding texture supports reconstruction.',
    's05l02':'Use cloning for straight structures and patterned texture that automatic healing tends to distort.',
    's05l03':'Use Remove/Content-Aware techniques for distractions when inpainted content can be checked against real context.',
    's05l04':'Use conservative portrait retouching where subject texture and identity must remain recognizable.',
    's05l05':'Use Curves-based dodge/burn for local dimensionality without permanently altering the raw photo layer.',
    's05l06':'Use Liquify and perspective tools for optical or geometric correction while documenting image integrity changes.',
    's05l07':'Use separate repair layers and an edit log for family archives, scanned prints and ethically documented restoration.',
    's06l01':'Use brush opacity, flow and hardness choices to control edges, gradients and masks instead of guessing at stroke strength.',
    's06l02':'Use pressure and brush dynamics for natural-looking pen-tablet drawing and repeated texture creation.',
    's06l03':'Use sampling and swatch libraries for consistent product colors, UI palettes and digital painting.',
    's06l04':'Use gradient/pattern fill layers for editable backgrounds, vignettes and repeated graphic motifs.',
    's06l05':'Use History Brush sparingly for session-based variants; prefer reversible masks for persistent revisions.',
    's06l06':'Use independent paint layers and value planning to build original illustrations with consistent lighting.',
    's07l01':'Use live text layers for posters, thumbnails and design systems where wording may change.',
    's07l02':'Use kerning, tracking and leading to fix poor visual rhythm and readability in client-facing typography.',
    's07l03':'Use vector shape paths for icons, panel backgrounds, adjustable borders and editable geometry.',
    's07l04':'Use Bézier paths for product cutouts and smooth logos where automated selections are imprecise.',
    's07l05':'Use path text for badges, labels and curved headlines while preserving editable type.',
    's07l06':'Use templates with replaceable Smart Objects for a repeatable campaign or client presentation.',
    's08l01':'Use histograms and Levels to diagnose tonal clipping before interpreting a photograph by screen brightness alone.',
    's08l02':'Use Curves for selective contrast and neutral color corrections that require channel-level precision.',
    's08l03':'Use local color-family corrections to fix casts or build a reproducible creative grade.',
    's08l04':'Use Camera Raw Smart Objects when exposure/white balance may need to be changed after the Photoshop composite is built.',
    's08l05':'Use mode, bit depth and ICC profile discipline to avoid color shifts between editing, export and print.',
    's08l06':'Use soft proofing before committing to an actual printer or narrow-gamut output destination.',
    's08l07':'Use controlled final-size sharpening and noise reduction in photographic delivery without introducing halos.',
    's09l01':'Use geometry and lighting planning to prevent believable individual assets from producing an implausible overall composite.',
    's09l02':'Use separate contact/cast shadows for believable product insertions and ground-plane integration.',
    's09l03':'Use edge and color matching when a good cutout still looks pasted onto a different background.',
    's09l04':'Use depth cues and local atmosphere for layered landscapes, posters and concept art.',
    's09l05':'Use displacement maps where a graphic must conform to fabric, paper or architectural surfaces.',
    's09l06':'Use frequency separation only where a precise diagnosis justifies separating texture from broad tonal changes.',
    's09l07':'Use systematic final review to catch compositing defects that global color grading alone cannot fix.',
    's10l01':'Use predictable source/work/export folders and packaging for revisable files transferred across computers.',
    's10l02':'Use Actions and Batch for repeated, tested production tasks with strict output naming safeguards.',
    's10l03':'Use Smart Object replacement to generate dozens of consistent visual mockup variants.',
    's10l04':'Use vetted scripts and plug-ins where a supported automation capability exceeds what Actions can reliably do.',
    's10l05':'Use format-appropriate export when exact transparency, dimensions and compression are delivery requirements.',
    's10l06':'Use preflight checklists when delivering for a particular print shop or handoff application.',
    's11l01':'Use performance diagnostics before changing Photoshop preferences or deleting scratch data.',
    's11l02':'Use guest-visible GPU diagnostics before deciding if a Windows VM is suitable for GPU-dependent Photoshop work.',
    's11l03':'Use controlled, reversible troubleshooting before resetting preferences or blaming document corruption.',
    's11l04':'Use missing-font/link/profile checks before editing source pixels to fix a delivery mismatch.',
    's11l05':'Use PSB, versioned saves and reopening tests for very large, long-lived layered productions.',
    's11l06':'Use a dependency inventory before planning a disconnected editing session or relying on model-based AI tools.',
    's12l01':'Use a controlled portrait capstone to demonstrate texture preservation, layer hygiene and readable before/after evidence.',
    's12l02':'Use restoration deliverables to show an honest separation between documented recovery and interpreted detail.',
    's12l03':'Use a product campaign to integrate masks, shadows, typography and export requirements in one brief.',
    's12l04':'Use a scene composite to prove camera, scale, mask, depth and light integration under final-size scrutiny.',
    's12l05':'Use a multi-format campaign to demonstrate portable assets and responsive design rather than blind scaling.',
    's12l06':'Use the final assignment as a repeatable evidence-based professional workflow from original files to checked handoff.'
    }
    assert len(uses)==len(LESSONS), 'Every lesson needs a substantive real-world application'
    for l in LESSONS:
        l['use']=uses[l['id']]
        l['completion'][1]='Explain the underlying mechanism in your own words: '+l['why']

    # Late-added reference rows need the same deterministic IDs as the base builder.
    import re
    for r in TOOLS:
        if 'id' not in r:r['id']='tool-'+re.sub('[^a-z0-9]+','-',r['title'].lower()).strip('-')
        if 'location' not in r:r['location']='Toolbar (grouped with Brush B; inspect options or Edit > Toolbar)'
        if 'status' not in r:r['status']='Modern built-in tool; verify toolbar layout'
    for coll,field,prefix in [(GLOSSARY,'term','glossar'),(RECIPES,'title','recipe')]:
        for r in coll:
            if 'id' not in r:r['id']=prefix+'-'+re.sub('[^a-z0-9]+','-',r[field].lower()).strip('-')
