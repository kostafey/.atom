# Your init script
#
# Atom will evaluate this file each time a new window is opened. It is run
# after packages are loaded/activated and after the previous editor state
# has been restored.
#
# An example hack to log to the console when each text editor is saved.
#
# atom.workspace.observeTextEditors (editor) ->
#   editor.onDidSave ->
#     console.log "Saved! #{editor.getPath()}"

atom.commands.add 'atom-text-editor', 'custom:hide', ->
  remote = require('electron').remote;
  window = remote.getCurrentWindow();
  window.minimize();

atom.commands.add 'atom-text-editor', 'revert-buffer:revert', ->
  editor = atom.workspace.getActiveTextEditor()
  return unless editor?.getPath()
  fs = require 'fs'
  fs.readFile editor.getPath(), (error, contents) ->
    editor.setText(contents.toString()) unless error
