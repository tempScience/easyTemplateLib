type Config = {
  /*
   * Resolveable ids to commitlint configurations to extend
   */
  extends?: string[];
  /*
   * Resolveable id to conventional-changelog parser preset to import and use
   */
  parserPreset?: string;
  /*
   * Resolveable id to package, from node_modules, which formats the output.
   */
  formatter: string;
  /*
   * Rules to check against
   */
  rules?: {[name: string]: Rule};
  /*
   * Functions that return true if commitlint should ignore the given message.
   */
  ignores?: ((message: string) => boolean)[];
  /*
   * Whether commitlint uses the default ignore rules.
   */
  defaultIgnores?: boolean;
};

const Configuration: Config = {
  /*
   * Resolve and load @commitlint/config-conventional from node_modules.
   * Referenced packages must be installed
   */
  extends: ['@commitlint/config-conventional'],
  /*
   * Resolve and load conventional-changelog-atom from node_modules.
   * Referenced packages must be installed
   */
  parserPreset: 'conventional-changelog-atom',
  /*
   * Resolve and load @commitlint/format from node_modules.
   * Referenced package must be installed
   */
  formatter: '@commitlint/format',
  /*
   * Any rules defined here will override rules from @commitlint/config-conventional
   */
  rules: {
    'type-enum': [2, 'always', ['foo']]
  },
  /*
   * Functions that return true if commitlint should ignore the given message.
   */
  ignores: [commit => commit === ''],
  /*
   * Whether commitlint uses the default ignore rules.
   */
  defaultIgnores: true
};

module.exports = Configuration;
