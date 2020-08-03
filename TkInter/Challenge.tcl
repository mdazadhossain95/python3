#############################################################################
# Generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#  Aug 03, 2020 02:27:37 PM CEST  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x450+650+150
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1055
    wm minsize $top 148 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra45 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 315 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 385 
    vTcl:DefineAlias "$top.fra45" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra45
    entry $site_3_0.ent46 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 244 
    vTcl:DefineAlias "$site_3_0.ent46" "Entry1" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but48 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text C 
    vTcl:DefineAlias "$site_3_0.but48" "Button1" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but49 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text CE 
    vTcl:DefineAlias "$site_3_0.but49" "Button2" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but50 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text 7 
    vTcl:DefineAlias "$site_3_0.but50" "Button3" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but51 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text 8 
    vTcl:DefineAlias "$site_3_0.but51" "Button3_1" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but52 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text 9 
    vTcl:DefineAlias "$site_3_0.but52" "Button3_2" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but53 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text + 
    vTcl:DefineAlias "$site_3_0.but53" "Button3_3" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but54 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text 4 
    vTcl:DefineAlias "$site_3_0.but54" "Button3_4" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but55 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text 5 
    vTcl:DefineAlias "$site_3_0.but55" "Button3_5" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but56 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text 6 
    vTcl:DefineAlias "$site_3_0.but56" "Button3_6" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but57 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text - 
    vTcl:DefineAlias "$site_3_0.but57" "Button3_7" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but58 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text 1 
    vTcl:DefineAlias "$site_3_0.but58" "Button3_8" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but59 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text 2 
    vTcl:DefineAlias "$site_3_0.but59" "Button3_9" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but60 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text 3 
    vTcl:DefineAlias "$site_3_0.but60" "Button3_10" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but61 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text * 
    vTcl:DefineAlias "$site_3_0.but61" "Button3_11" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but62 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text 0 
    vTcl:DefineAlias "$site_3_0.but62" "Button3_12" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but63 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text = 
    vTcl:DefineAlias "$site_3_0.but63" "Button3_13" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but64 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text / 
    vTcl:DefineAlias "$site_3_0.but64" "Button3_14" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.ent46 \
        -in $site_3_0 -x 0 -relx 0.114 -y 0 -rely 0.032 -width 244 \
        -relwidth 0 -height 44 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but48 \
        -in $site_3_0 -x 0 -relx 0.119 -y 0 -rely 0.222 -width 56 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but49 \
        -in $site_3_0 -x 0 -relx 0.268 -y 0 -rely 0.222 -width 56 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but50 \
        -in $site_3_0 -x 0 -relx 0.119 -y 0 -rely 0.333 -width 56 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but51 \
        -in $site_3_0 -x 0 -relx 0.27 -y 0 -rely 0.333 -width 56 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but52 \
        -in $site_3_0 -x 0 -relx 0.426 -y 0 -rely 0.333 -width 56 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but53 \
        -in $site_3_0 -x 0 -relx 0.577 -y 0 -rely 0.333 -width 56 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but54 \
        -in $site_3_0 -x 0 -relx 0.119 -y 0 -rely 0.441 -width 56 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but55 \
        -in $site_3_0 -x 0 -relx 0.27 -y 0 -rely 0.441 -width 56 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but56 \
        -in $site_3_0 -x 0 -relx 0.426 -y 0 -rely 0.441 -width 56 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but57 \
        -in $site_3_0 -x 0 -relx 0.577 -y 0 -rely 0.441 -width 56 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but58 \
        -in $site_3_0 -x 0 -relx 0.119 -y 0 -rely 0.549 -width 56 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but59 \
        -in $site_3_0 -x 0 -relx 0.27 -y 0 -rely 0.549 -width 56 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but60 \
        -in $site_3_0 -x 0 -relx 0.426 -y 0 -rely 0.549 -width 56 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but61 \
        -in $site_3_0 -x 0 -relx 0.577 -y 0 -rely 0.549 -width 56 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but62 \
        -in $site_3_0 -x 0 -relx 0.119 -y 0 -rely 0.66 -width 56 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but63 \
        -in $site_3_0 -x 0 -relx 0.27 -y 0 -rely 0.66 -width 116 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but64 \
        -in $site_3_0 -x 0 -relx 0.577 -y 0 -rely 0.66 -width 56 -relwidth 0 \
        -height 33 -relheight 0 -anchor nw -bordermode ignore 
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra45 \
        -in $top -x 0 -relx 0.15 -y 0 -rely 0.111 -width 0 -relwidth 0.642 \
        -height 0 -relheight 0.7 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
