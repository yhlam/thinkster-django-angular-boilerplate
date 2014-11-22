(function() {
  'use strict';

  angular
    .module('thinkster.post', [
      'thinkster.post.controllers',
      'thinkster.post.directives',
      'thinkster.post.services'
    ]);

  angular
    .module('thinkster.post.controllers', []);

  angular
    .module('thinkster.post.directives', ['ngDialog']);

  angular
    .module('thinkster.post.services', []);
})();
